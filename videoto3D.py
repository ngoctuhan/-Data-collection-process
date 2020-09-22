import cv2
import numpy as np 

class Videoto3D:

    def __init__(self,  width , height , depth = 24):

        self.width = width
        self.height = height
        self.depth = depth
       
    def get_frames(self, filename, color=True, skip=True):
        '''
        Get a array frame from a video
        Input:
        
        - filename: path of the file (str)
        - color   : number chanle of image (option RGB|GRAY)
        - skip    : bool

        Output:

        - Array image with shape ( n_frame, with, height, chanel)
      '''
        
        
        cap = cv2.VideoCapture(filename)
        nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT) # give n frame
        # print(nframe)
        if (color == True):
            frames = [int(x) * nframe / self.depth for x in range(self.depth)]
        else:
            frames = [int(x) * nframe / self.depth for x in range(self.depth)]
        
        framearray = []
            
        for i in range(self.depth):

            cap.set(cv2.CAP_PROP_POS_FRAMES, frames[i])
            ret, prvs = cap.read()
                
            if prvs is None:
                # print(frames[i])
                continue
            prvs = cv2.resize(prvs, (self.height, self.width)) 
            if color:
                framearray.append(prvs)
            else:
                framearray.append(cv2.cvtColor(prvs, cv2.COLOR_BGR2GRAY))
        cap.release()
        
        if len(framearray) == 0:
            print(filename)
            return None
        while len(framearray) != self.depth:
            framearray.append(framearray[-1])
        framearray = np.asanyarray(framearray)
        return framearray

      


# import pandas as pd #
# import os
# file_train = 'dataset_split/train_file.csv'
# file_test  = 'dataset_split/test_file.csv'
# df_train =  pd.read_csv(file_train)

# X_train =  df_train['file'].values
# y_train = df_train['label'].values

# df_test  = pd.read_csv(file_test)

# X_test = df_test['file'].values
# y_test = df_test['label'].values
# vd = Videoto3D(224, 224, 24)
# for file in X_test:
#     filename = os.path.join('SL-PTIT-50', file)
#     vd.get_frames(filename)