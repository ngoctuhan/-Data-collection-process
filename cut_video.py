import cv2 
import os
import time
import pandas as pd
import numpy as np
import re
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
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

def get_duration(input_video):
    cmd = ["ffprobe", "-i", input_video, "-show_entries", "format=duration",
           "-v", "quiet", "-sexagesimal", "-of", "csv=p=0"]
    return subprocess.check_output(cmd).decode("utf-8").strip()

def mkdir(FOLDER):
    if os.path.exists(os.path.join('SL-PTIT-50', FOLDER)) == False:
        os.mkdir(os.path.join('SL-PTIT-50', FOLDER))

def trim_video(file, person, part):

    '''
    chuẩn hóa thời gian từng hành động trong video 
    '''
    root_path = 'dataset/' +  person

    video_file =  person + '_video_Part_' + str(part) +  '.mp4'
    video_file = os.path.join(root_path,'VIDEO' ,video_file)

    file_eaf   = file.split('.')[0] + '.eaf'
    file_eaf = os.path.join(root_path, file_eaf)
    time_add   = get_time_offset(file_eaf) 
    file = os.path.join(root_path, file)

    TIME_DURATION = []
    CLASSES    = []
    with open(file, 'r') as f:
        lines =  f.readlines()
        
        for i, line in enumerate(lines):
            if i == 0: 
                continue
            else:
                line_split =  line.split('\t')
                START = round(float(line_split[0]) + time_add ) 
                # START =  float(line_split[0]) + time_add
                END = round(float(line_split[1]) + time_add )
                # END = float(line_split[1]) + time_add
                TIME_DURATION.append([START, END])

                CLASSES.append(line_split[2].split('\n')[0].lower().split(" ")[0])
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
        video_out = person + "_" +CLASSES[i]+"_" +str(j)  + '.mp4'
        video_out = os.path.join('SL-PTIT-50', CLASSES[i], video_out)
        ffmpeg_extract_subclip(video_file, time[0], time[1], targetname=video_out)

# for i in range(1, 5):
#     path = 'N10_Right_Part_{}.txt'.format(str(i))
#     trim_video(path, 'N10', i)
  

for i in range(1, 3):
    path = 'N12_Part{}.txt'.format(str(i))
    trim_video(path, 'N12', i)

# path = 'N9_Part1.txt'
# trim_video(path, 'N9', 1)