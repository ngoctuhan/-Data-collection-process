"""
use method 'write_labels' to export labeled csv files
"""

import pandas as pd
import numpy as np
import re

pattern_time = r'<.*TIME_ORIGIN=\"(\d+)\".*/>'


def get_time_offset(eaf_file):
    """
    Get offset from ELAN save file eaf.
    :param eaf_file: ELAN save file
    :return: offset
    """

    result = None

    with open(eaf_file, 'r') as eaf:
        lines = eaf.readlines()

        for line in lines:
            result = re.search(pattern_time, line)
            if result is not None:
                result = int(result.group(1)) / 1000.
                break

        if result is None:
            result = 0

    return result


def get_labels(timestamps_txt, time_offset, n_samples, df):
    """
    Get label and sub-label for the whole data frame.
    :param timestamps_txt: ELAN export file
    :param time_offset: offset
    :param n_samples: number of samples in data frame
    :param df: data frame
    :return: label and sub label
    """
    label_np = np.zeros(n_samples, dtype=object)

    with open(timestamps_txt, "r") as txt_file:
        lines = txt_file.readlines()

        for i, line in enumerate(lines):
            if i == 0 or line == '\n':
                continue

            line = line.replace('\n', '')
            info = line.split('\t')

            start = float(info[0])
            end = float(info[1])

            label = None

            if (info[2] != ''):
                label = info[2].strip()

            filter_df1 = df['times'] >= (start + time_offset)
            filter_df2 = df['times'] <= (end + time_offset)
            data = df.where(filter_df1 & filter_df2, inplace=False)
            data.dropna(inplace=True, how='all')
            indices = data.index

            if len(indices) == 0:
                continue

            print('Start time: {}; End time: {}'.format(start, end))

            start_idx = indices[0]
            end_idx = indices[-1]

            if label is not None:
                label_np[start_idx:end_idx] = label

    label_np[np.where(label_np == 0)[0]] = 'null'
    return label_np


def write_labels(input_csv, timestamps_txt, eaf_file, output_csv=None, input_csv_sep=',', output_csv_sep=','):
    """
    Take 3 files as inputs and write labeled data file.
    :param input_csv: unlabeled csv data file with relative timestamp in second
        columns are: timestamp, accX, accY, accZ, gyrX, gyrY, gyrZ
    :param timestamps_txt: ELAN exported file .txt
    :param eaf_file: ELAN save file .eaf
    :param output_csv: output csv file name, default to inputname_labeled.csv
    :param input_csv_sep: input csv separator
    :param output_csv_sep: output csv separator
    """
    if output_csv is None:
        output_csv = '.'.join(input_csv.split('.')[:-1]) + '_labeled.csv'

    df = pd.read_csv(input_csv, delimiter=input_csv_sep)
    output = df

    time_offset = get_time_offset(eaf_file=eaf_file)

    print('offset: ' + str(time_offset))

    label_np = get_labels(timestamps_txt, time_offset, len(output), output)
    ncols = output.shape[-1]
    output[ncols] = label_np

    output.to_csv(output_csv,
                  sep=output_csv_sep,
                  header=['times', 'accX', 'accY', 'accZ',
                          'gyroX', 'gyroY', 'gyroZ',
                          'label'],
                  encoding='utf-8',
                  index=False)
    print('DONE')
    return True

write_labels(
    timestamps_txt='dataset/N1/N1-1-5.txt', # file .txt export from elan software
    eaf_file='dataset/N1/N1-1-5.eaf', # file .eaf export from elan software
    input_csv='dataset/N1/N1-R-1-5.csv' # file .csv dataset linked with video 
)