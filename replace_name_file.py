import os
from txt2csv import timestamp2offset


def rename_file(person_id):

    folder = 'dataset'
    sensor_R = os.path.join(folder, person_id,'H2C4')
    sensor_L = os.path.join(folder, person_id,'E67E')
    video    = os.path.join(folder, person_id,'VIDEO')

    count_part =  len(os.listdir(sensor_L))

    for i, file in enumerate(os.listdir(sensor_L)):
        print(file)
        file_old = os.path.join(sensor_L, file)
        file_replace = os.path.join(sensor_L, person_id + "_" + "sensor_L_Part_" + str(i+1) + ".txt")
        os.rename(file_old, file_replace) 
        timestamp2offset(file_replace,file_replace.split(".")[0] + '.csv')

    for i, file in enumerate(os.listdir(sensor_R)):
        print(file)
        file_old = os.path.join(sensor_R, file)
        file_replace = os.path.join(sensor_R, person_id + "_" + "sensor_R_Part_" + str(i+1) + '.txt') 
        os.rename(file_old, file_replace)   
        timestamp2offset(file_replace,file_replace.split(".")[0] + '.csv')
 
    for i, file in enumerate(os.listdir(video)):
        print(file)
        file_old = os.path.join(video, file)
        file_replace = os.path.join(video, person_id + "_" + "video_Part_" + str(i+1) + ".mp4")
        os.rename(file_old, file_replace) 

rename_file("N12")


