import os
import numpy as np 
import pandas as pd 

class Config:

    '''
    Class have all parameter default
    '''
    # dataset SENSOR
    TIME_STEPS = 128
    PADDING = 'medium'

    # par for training 
    batch_size = 16
    epouchs  = 50


class SENSOR_LOADER:

    def __init__(self, time_steps: int, padding: str, mode = 'all', acc = True, gcc = True):

        '''
        Load dataset sensor 
        Input: 
        + time_steps: number samples will be load, recomend: 128 samples 
        + padding: if sample is not enough time_steps, will be add values, METHOD add value (medium|zero)
        + mode: just load righ-hand, or all (value: all|right)
        + using acc sensor (yes|no)
        + using gcc sensor (yes|no)

        Output: using acc or gcc : array with shape (1, 3 ,time_steps) with mode = right
                                 (1, 6, time_steps) wiht mode = right

                using acc and gcc: array with shape (1, 6 ,time_steps) with mode = right
                                 (1, 12, time_steps) wiht mode = right
        '''
        self.cfg = Config()
        if time_steps is None:
            time_steps = self.cfg.TIME_STEPS
        else:  
            self.time_steps = time_steps

        if padding is None:
            self.padding = self.cfg.PADDING
        elif padding == 'medium' or padding == 'zero':
            raise Exception("Dont have your options")
        else:
            self.padding = padding
        self.mode = mode
        self.acc  = acc
        self.gcc  = gcc

    def load_data(self, file_path):

        '''Get dataset with input is path of file'''
        df =  pd.read_csv(file_path)
        
        acc_data, gcc_data = None, None
       
        n_sample = df.values.shape[0] - 1 
        frames = [int(x) *  n_sample / self.time_steps for x in range(self.time_steps)]
        
        if self.acc:
            acc_data = df.values[:, 1:4]
        if self.gcc:
            gcc_data = df.value[:, 4:]
        

        




        

        