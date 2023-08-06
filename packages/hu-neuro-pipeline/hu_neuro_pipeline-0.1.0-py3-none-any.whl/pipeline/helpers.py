from collections import Counter
from itertools import chain, combinations
from os import path
from sys import exit

import chardet
import numpy as np
import pandas as pd
from mne import combine_evoked, pick_channels, set_bipolar_reference
from mne.channels import (combine_channels, make_standard_montage,
                          read_custom_montage)
from mne.preprocessing import ICA


def add_heog_veog(raw, heog_channels='auto', veog_channels='auto'):
    """Adds virtual HEOG and VEOG using default or non-default EOG names."""

    # Add bipolar HEOG channel
    if heog_channels is not None:
        if heog_channels == 'auto':
            heog_channels = ['F9', 'F10', 'Afp9', 'Afp10']
        raw = add_eog(raw, heog_channels, new_name='HEOG')

    # Add bipolar VEOG channel
    if veog_channels is not None:
        if veog_channels == 'auto':
            veog_channels = ['Fp1', 'FP1', 'Auge_u', 'IO1']
        raw = add_eog(raw, veog_channels, new_name='VEOG')

    return raw


def add_eog(raw, channels, new_name):
    """Computes a single bipolar EOG channel from a list of possible names."""

    # Check that exactly two of the provided channels are in the data
    channels = [ch for ch in channels if ch in raw.ch_names]
    if len(channels) != 2:
        exit(f'Could not find two channels for computing bipolar {new_name}. '
             'Please provide different channel names or choose None.')

    # Compute bipolar EOG channel
    anode = channels[0]
    cathode = channels[1]
    print(f'Adding bipolar channel {new_name} ({anode} - {cathode})')
    raw = set_bipolar_reference(
        raw, anode, cathode, new_name, drop_refs=False, verbose=False)
    raw = raw.set_channel_types({new_name: 'eog'})

    return raw


def apply_montage(raw, montage):
    """Reads electrode positions from custom file or standard montage."""

    # Load custom montage from file
    if path.isfile(montage):
        print(f'Loading custom montage from {montage}')
        digmontage = read_custom_montage(montage)

    # Or load standard montage
    else:
        print(f'Loading standard montage {montage}')
        digmontage = make_standard_montage(montage)

    # Make sure that EOG channels are of the eog type
    eog_channels = set(['HEOG', 'VEOG', 'IO1', 'IO2', 'Afp9', 'Afp10'])
    for channel_name in eog_channels:
        if channel_name in raw.ch_names:
            raw.set_channel_types({channel_name: 'eog'})

    # Get EEG channels that are not in the montage
    raw_channels = set(raw.copy().pick_types(eeg=True).ch_names)
    montage_channels = set(digmontage.ch_names)
    drop_channels = list(raw_channels - montage_channels)
    if drop_channels != []:
        print(f'Removing channels that are not in the montage {drop_channels}')
        raw.drop_channels(drop_channels)

    # Apply montage
    raw.set_montage(digmontage)


def correct_ica(raw, n_components=15, random_seed=1234, method='fastica'):
    """Corrects ocular artifacts using ICA and automatic component removal."""

    # Run ICA on a copy of the data
    raw_filt_ica = raw.copy()
    raw_filt_ica.load_data().filter(l_freq=1, h_freq=None, verbose=False)
    ica = ICA(
        n_components, random_state=random_seed, method=method, max_iter='auto')
    ica.fit(raw_filt_ica)

    # Remove bad components from the raw data
    eog_indices, _ = ica.find_bads_eog(
        raw, ch_name=['HEOG', 'VEOG'], verbose=False)
    ica.exclude = eog_indices
    raw = ica.apply(raw)


def correct_besa(raw, besa_file):
    """Corrects ocular artifacts using a pre-computed MSEC (BESA) matrix."""

    # Read BESA matrix
    print(f'Doing ocular correction with MSEC (BESA)')
    besa_matrix = pd.read_csv(besa_file, delimiter='\t', index_col=0)

    # Get EEG channel labels that are present in the data
    eeg_channels = raw.copy().pick_types(eeg=True).ch_names

    # Convert EEG channel labels to uppercase
    eeg_upper = pd.Series(eeg_channels).str.upper().values

    # Also convert BESA matrix labels to uppercase
    besa_matrix.index = besa_matrix.index.str.upper()
    besa_matrix.columns = besa_matrix.columns.str.upper()

    # Match so that the BESA matrix only contains channels that are in the data
    row_channels = [ch for ch in besa_matrix.index if ch in eeg_upper]
    col_channels = [ch for ch in besa_matrix.columns if ch in eeg_upper]
    besa_matrix = besa_matrix.reindex(index=row_channels, columns=col_channels)

    # Apply BESA matrix to the data
    eeg_data, _ = raw[eeg_channels]
    eeg_data = besa_matrix.values.dot(eeg_data)
    raw[eeg_channels] = eeg_data


def read_log(log_file, skip_log_rows=None, skip_log_conditions=None):
    """Reads the behavioral log file with information about each EEG trial."""

    # Check if data are already in a DataFrame
    if isinstance(log_file, pd.DataFrame):
        log = log_file
    else:

        # Detect file encoding
        with open(log_file, 'rb') as f:
            data = f.read()
        chardet_res = chardet.detect(data)
        encoding = chardet_res['encoding']

        # Read into DataFrame
        if '.csv' in log_file:
            log = pd.read_csv(log_file, encoding=encoding)
        else:
            log = pd.read_csv(log_file, delimiter='\t', encoding=encoding)

    # Remove rows via indices (e.g., if the EEG was paused accidently)
    if skip_log_rows is not None:
        log = log.drop(skip_log_rows)

    # Remove rows via conditions (e.g., for filler stimuli without triggers)
    if skip_log_conditions is not None:
        assert isinstance(skip_log_conditions, dict), \
            '"skip_log_conditions" must be a dict ({column: [conditions]})'
        for col, values in skip_log_conditions.items():
            if not isinstance(values, list):
                log = log[log[col] != values]
            else:
                log = log[~log[col].isin(values)]

    return log


def get_bads(
        epochs, reject_peak_to_peak=None, reject_flat=None, percent_bad=0.05):
    """Detects bad epochs/channels based on peak-to-peak and flat amplitude."""

    # Convert thresholds to volts in dicts
    if reject_peak_to_peak is not None:
        reject_peak_to_peak = {'eeg': reject_peak_to_peak * 1e-6}
    if reject_flat is not None:
        reject_flat = {'eeg': reject_flat * 1e-6}

    # Reject on a copy of the data
    epochs_rej = epochs.copy().drop_bad(reject_peak_to_peak, reject_flat)
    drop_log = [elem for elem in epochs_rej.drop_log if elem != ('IGNORED',)]
    bad_tuples = [(ix, elem) for ix, elem in enumerate(drop_log) if elem != ()]

    # Get bad epochs from tuples
    bad_ixs = [bad_tuple[0] for bad_tuple in bad_tuples]

    # Get channels that are responsible for the bad epochs
    bad_channels = [bad_tuple[1] for bad_tuple in bad_tuples]
    bad_channels = list(sum(bad_channels, ()))  # Makes it a flat list

    # See which channels are responsible for at least X percent of epochs
    counts = Counter(bad_channels)
    bad_channels = [ch for ch, count in counts.items()
                    if count > len(epochs) * percent_bad]

    return (bad_ixs, bad_channels)


def compute_single_trials(epochs, components, bad_ixs=None):
    """Computes mean ERP amplitude for a dict of multiple components."""

    # Compute single trial mean ERP amplitudes for each component
    components_df = pd.DataFrame(components)
    for _, component in components_df.iterrows():
        compute_component(
            epochs, component['name'], component['tmin'],
            component['tmax'], component['roi'], bad_ixs)

    return epochs.metadata


def compute_component(epochs, name, tmin, tmax, roi, bad_ixs=None):
    """Computes mean ERP amplitude for single component."""

    # Create virtual channel for the average in the region of interest
    print(f'Computing single trial ERP amplitudes for {name}')
    roi_dict = {name: pick_channels(epochs.ch_names, roi)}
    backup_verbose = epochs.verbose
    epochs.verbose = False
    epochs_roi = combine_channels(epochs, roi_dict)
    epochs.add_channels([epochs_roi], force_update_info=True)
    epochs.set_channel_types({name: 'misc'})
    epochs.verbose = backup_verbose

    # Compute mean amplitudes by averaging across the relevant time window
    epochs_roi.crop(tmin, tmax)
    df = epochs_roi.to_data_frame()
    mean_amp = df.groupby('epoch')[name].mean()

    # Set ERPs for bad epochs to NaN
    if bad_ixs is not None:
        if isinstance(bad_ixs, int):
            bad_ixs = [bad_ixs]
        mean_amp[bad_ixs] = np.nan

    # Add as a new column to the original metadata
    epochs.metadata.reset_index(drop=True, inplace=True)
    epochs.metadata = pd.concat([epochs.metadata, mean_amp], axis=1)


def compute_evokeds(
        epochs, condition_cols=None, bad_ixs=[], participant_id=None):
    """Computes condition averages (evokeds) based on triggers or metadata."""

    # Prepare emtpy list for storing
    all_evokeds = []
    all_evokeds_dfs = []

    # Always use EEG and misc (component) channels for averaging
    picks = ['eeg', 'misc']

    # If no condition_cols were provided, use the events from the epochs
    if condition_cols is None:

        # Compute evokeds
        epochs_good = epochs.copy().drop(bad_ixs, verbose=False)
        evokeds = epochs_good.average(picks, by_event_type=True)
        all_evokeds.append(evokeds)

        # Convert to DataFrame
        evokeds_df = create_evokeds_df(evokeds, participant_id=participant_id)
        all_evokeds_dfs.append(evokeds_df)

    # Otherwise use condition_cols
    else:

        # Create the powerset (all possible main effects and interactions)
        c = condition_cols if isinstance(condition_cols, list) \
            else [condition_cols]
        powerset = chain.from_iterable(
            combinations(c, r) for r in range(1, len(c) + 1))

        # Iterate over the possible main effects and interactions
        for cols in powerset:
            cols = list(cols)

            # Compute evokeds
            epochs_update = update_events(epochs, cols)
            epochs_update.drop(bad_ixs, verbose=False)
            evokeds = epochs_update.average(picks, by_event_type=True)
            all_evokeds = all_evokeds + evokeds

            # Convert to DataFrame
            trials = epochs.metadata
            evokeds_df = create_evokeds_df(
                evokeds, cols, trials, participant_id)

            # Append info about averaging
            value = ' * '.join(cols)
            evokeds_df.insert(loc=1, column='average_by', value=value)
            all_evokeds_dfs.append(evokeds_df)

    # Combine DataFrames
    all_evokeds_dfs.reverse()
    all_evokeds_df = pd.concat(all_evokeds_dfs, ignore_index=True)

    return all_evokeds, all_evokeds_df


def update_events(epochs, cols):
    """Updates the events/event_id structures using cols from the metadata."""

    # Generate event codes for the relevant columns
    cols_df = pd.DataFrame(epochs.metadata[cols])
    cols_df = cols_df.astype('str')
    ids = cols_df.agg('/'.join, axis=1)
    codes = ids.astype('category').cat.codes

    # Create copy of the data with the new event codes
    epochs_update = epochs.copy()
    epochs_update.events[:, 2] = codes
    epochs_update.event_id = dict(zip(ids, codes))

    return epochs_update


def create_evokeds_df(evokeds, cols=None, trials=None, participant_id=None):
    """Converts mne.Evoked into a pd.DataFrame with metadata."""

    # Convert all evokeds to a single DataFrame
    scalings = {'eeg': 1e6, 'misc': 1e6}
    evokeds_dfs = [evoked.to_data_frame(scalings=scalings)
                   for evoked in evokeds]
    evokeds_df = pd.concat(evokeds_dfs, ignore_index=True)

    # Optionally add columns from the metadata
    n_samples = len(evokeds[0].times)
    if cols is not None:
        assert trials is not None, 'Must provide trials (metadata) with cols'
        cols_df = pd.DataFrame(trials[cols])
        cols_df = cols_df.astype('str')
        cols_df = cols_df.drop_duplicates()
        cols_df = cols_df.loc[cols_df.index.repeat(n_samples)]
        cols_df = cols_df.reset_index(drop=True)
        evokeds_df = pd.concat([cols_df, evokeds_df], axis=1)

    # Otherwise add comments from evokeds (assumed to contain event IDs)
    else:
        comments = [evoked.comment for evoked in evokeds]
        comments = np.repeat(comments, n_samples)
        evokeds_df.insert(loc=0, column='event_id', value=comments)

    # Optionally add participant_id
    if participant_id is not None:
        evokeds_df.insert(loc=0, column='participant_id', value=participant_id)

    return evokeds_df


def compute_grands(evokeds_per_participant):
    """Averages evokeds of all participants into grand averages."""

    # Average across participants for each condition
    evokeds_per_condition = list(map(list, zip(*evokeds_per_participant)))
    grands = [combine_evoked(x, weights='nave') for x in evokeds_per_condition]

    # Add meaningful comments
    comments = [x[0].comment for x in evokeds_per_condition]
    for grand, comment in zip(grands, comments):
        grand.comment = comment

    return grands


def compute_grands_df(evokeds_df):
    """Averages evoked DataFrames of all participants into grand averages."""

    # Average by condition columns (between participant_id and time)
    time_col_ix = evokeds_df.columns.get_loc('time')
    participant_id_ix = 1
    group_cols = list(evokeds_df.columns[participant_id_ix:(time_col_ix + 1)])
    grands_df = evokeds_df.groupby(group_cols, dropna=False).mean()

    # Convert conditions from index back to columns
    grands_df = grands_df.reset_index()

    return grands_df


def check_participant_input(input, participant_ids):
    """Converts different inputs (e.g., dict) into a per-participant list."""

    # If it's a dict, convert to list
    if isinstance(input, dict):
        participant_dict = {id: None for id in participant_ids}
        for id, values in input.items():
            assert id in participant_ids, \
                f'Participant ID {id} is not in vhdr_files'
            participant_dict[id] = values
        return participant_dict.values()

    # If it's a list of list, it must have the same length as participant_ids
    elif is_nested_list(input):
        assert len(input) == len(participant_ids), \
            'Input lists must have the same length'
        return input

    # Otherwise all participants get the same values
    else:
        return [input] * len(participant_ids)


def is_nested_list(input):
    """Checks if a list is nested, i.e., contains at least one other list."""

    # Check if there is any list in the list
    if isinstance(input, list):
        return any(isinstance(elem, list) for elem in input)
    else:
        return False
