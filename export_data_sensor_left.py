import os
import pandas as pd 
import numpy as np 


def mkdir(FOLDER):
    if os.path.exists(os.path.join('F:\Current Project\Dataset Sign Language\SL-PTIT-SENSOR-LEFT', FOLDER)) == False:
        os.mkdir(os.path.join('F:\Current Project\Dataset Sign Language\SL-PTIT-SENSOR-LEFT', FOLDER))

def get_data(df, ST, EN, adjust_time = 0):

    filter_df1 = df['times'] >= ST
    filter_df2 = df['times'] <= (EN+ adjust_time)
    data = df.where(filter_df1 & filter_df2, inplace=False)
    data.dropna(inplace=True, how='all')
    return data

def get_file_txt(folder):
    '''
    Get a list file txt in a folder
    Input: Path of folder
    Output: list file
    '''
    list_file = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            list_file.append(file)
    return list_file

def get_time_adjust(person, part):

    path_file_adjust = os.path.join('dataset',person, '{}_Distance'.format(person), '{}_Distance_Part_{}.txt'.format(person, part))

    with open(path_file_adjust, 'r') as file:

        lines = file.readlines()

        line = lines[1]
        time_adj = abs(float(line.split('\t')[0]) - float(line.split('\t')[1]))

        print(line.split('\t'))
        if line.split('\t')[2] == 'LR': 
            return time_adj
        if line.split('\t')[2] == 'RL':
            return -1* time_adj

def get_data_sensor(sensor_name, file_label, person, part):
    print("Part: ", part)
    '''
    - Get data sensor after labeled
    - Save file each sample into a file
    Input:
        + sensor_name : L | R 
        + file_label  : file txt after labeled
        + person      : id_person from N1 to N11
        + part        : part of video
    Output:
        Dont have output
    '''
    if sensor_name == 'L': # E67E 
        path_df = 'dataset/' + person + '/' + 'E67E'
        time_adj =  get_time_adjust(person, part)
        raw_data_path =  os.path.join(path_df, '{}_sensor_L_Part_{}.csv'.format(person, str(part)))
    else:
        path_df = 'dataset/' + person + '/' + 'H2C4'
        raw_data_path =  os.path.join(path_df, '{}_sensor_R_Part_{}.csv'.format(person, str(part)))
    
    df =  pd.read_csv(raw_data_path)
    labeled_file = os.path.join('dataset', person, file_label)
    TIME_DURATION = []
    CLASSES    = []
   
    with open(labeled_file, 'r') as f:
        lines =  f.readlines()
        
        for i, line in enumerate(lines):
            if i == 0: 
                continue
            else:
                line_split =  line.split('\t')
                START = float(line_split[0])  + time_adj - 0.5
                END = float(line_split[1])  + time_adj + 0.75
                TIME_DURATION.append([START, END]) 
                CLASSES.append(line_split[2].split('\n')[0].lower().split(' ')[0])

    bf = ""
    j = 0
    for i,time in enumerate(TIME_DURATION):
        mkdir(CLASSES[i])
        
        if bf != CLASSES[i]:
            bf = CLASSES[i]
            j = 0
        else:
            j += 1
        csv_out = person + "_" +CLASSES[i]+"_" +str(j)+'_'+ sensor_name  + '.csv'
        csv_out = os.path.join('F:\Current Project\Dataset Sign Language\SL-PTIT-SENSOR-LEFT', CLASSES[i], csv_out)
    
        data = get_data(df, time[0], time[1])
        data.to_csv(csv_out, encoding='utf-8', index=False)
        
if __name__ == '__main__':

    for i in range(11,12):
        person =  'N{}'.format(str(i))
        print(person)
        list_file = get_file_txt('dataset/' + person)
        for i, file in enumerate(list_file): 
            get_data_sensor('L',file, person, i+1)

