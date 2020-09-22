import numpy as np #
import pandas as pd
from random import sample
import os 


# labels  = []
X_train = []
y_train = []
X_test  = []
y_test  = []

for folder in os.listdir('SL-PTIT-50'):

    label = folder
    
    files = os.listdir(os.path.join('SL-PTIT-50', folder))

    files = [label + '/' + file for file in files]
    sample_standard =  160

    if len(files) > sample_standard +  0.35 * sample_standard:
        sample_train = round(0.6 * len(files))
        sample_test  = len(files) - sample_train
    elif len(files) > sample_standard +  0.25 * sample_standard:
        sample_train = round(0.7 * len(files))
        sample_test  = len(files) - sample_train
    else:
        sample_train = round(0.75 * len(files))
        sample_test  = len(files) - sample_train

    test = sample(files, sample_test)
    train = list(filter(lambda i: i not in test , files))

    print(len(train), ' ', sample_train)
    print(len(files))
   
    X_train += train
    X_test  += test
    y_train += [label] * sample_train
    y_test  += [label] * sample_test
    # break


X_train =  np.array(X_train).reshape(-1, 1)

X_test  =  np.array(X_test).reshape(-1, 1)
# labels  =  np.array(labels).reshape(-1, 1)
y_train =  np.array(y_train).reshape(-1, 1)

y_test  = np.array(y_test).reshape(-1, 1)

data_train = np.concatenate((X_train, y_train), axis=1)
data_test  = np.concatenate((X_test, y_test), axis=1)

colums = ['file', 'label']
df1 = pd.DataFrame(data_train, columns=colums)
df1.to_csv(os.path.join('dataset_split', 'train_file.csv'), encoding='utf-8',index=False)

df2 = pd.DataFrame(data_test, columns=colums)
df2.to_csv(os.path.join('dataset_split', 'test_file.csv'), encoding='utf-8',index=False)