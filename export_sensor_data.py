import os
import pandas as pd 
import numpy as np 


def mkdir(FOLDER):
    if os.path.exists(os.path.join('SL-PTIT-50-SENSOR', FOLDER)) == False:
        os.mkdir(os.path.join('SL-PTIT-50-SENSOR', FOLDER))

def get_data(df, ST, EN, adjust_time = 0):

    filter_df1 = df['times'] >= ST
    filter_df2 = df['times'] <= (EN+ adjust_time)
    data = df.where(filter_df1 & filter_df2, inplace=False)
    data.dropna(inplace=True, how='all')
    return data
    # print(data.values)

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

def get_data_sensor(sensor_name, file_label, person, part):
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
        
        raw_data_path =  os.path.join(path_df, '{}_sensor_L_Part_{}.csv'.format(person, str(part)))
    else:
        path_df = 'dataset/' + person + '/' + 'H2C4'
        raw_data_path =  os.path.join(path_df, '{}_sensor_R_Part_{}.csv'.format(person, str(part)))
    
    df =  pd.read_csv(raw_data_path)

    labeled_file = os.path.join('dataset', person, file_label)
    print(labeled_file)
    TIME_DURATION = []
    CLASSES    = []
    with open(labeled_file, 'r') as f:
        lines =  f.readlines()
        
        for i, line in enumerate(lines):
            if i == 0: 
                continue
            else:
                # print(line)
                line_split =  line.split('\t')
                START = float(line_split[0]) - 0.5
                # START =  float(line_split[0]) + time_add
                END = float(line_split[1]) + 0.75
                # END = float(line_split[1]) + time_add
                TIME_DURATION.append([START, END]) 

                CLASSES.append(line_split[2].split('\n')[0].lower().split(' ')[0])

    bf = ""
    j = 0
    for i,time in enumerate(TIME_DURATION):
    # ! ffmpeg -i input.mp4 -ss 01:19:27 -to 02:18:51 -c:v copy -c:a copy output.mp4
        # time = TIME_DURATION[i]
        mkdir(CLASSES[i])
        
        if bf != CLASSES[i]:
            bf = CLASSES[i]
            j = 0
        else:
            j += 1
        csv_out = person + "_" +CLASSES[i]+"_" +str(j)+'_'+ sensor_name  + '.csv'
        csv_out = os.path.join('SL-PTIT-50-SENSOR', CLASSES[i], csv_out)
    
        data = get_data(df, time[0], time[1])
        data.to_csv(csv_out, encoding='utf-8', index=False)
        
        # ffmpeg_extract_subclip(video_file, time[0], time[1], targetname=video_out)

if __name__ == '__main__':
    for i in range(12, 13):
        person =  'N{}'.format(str(i))
        list_file = get_file_txt('dataset/' + person )
        for i, file in enumerate(list_file):
            
            get_data_sensor('R',file, person, i+1)
            # print(file)

# print(get_file_txt('dataset/N2'))