import pandas as pd
import numpy as np #
import os 

num_stand =  160

list_name = []
list1= []
need = []
for folder in os.listdir('SL-PTIT-50'):
    list1.append(len(os.listdir(os.path.join('SL-PTIT-50', folder))))
    list_name.append(folder)
    need.append(list1[-1] -  num_stand)
    if need[-1] > 0:
        need[-1] = 0

sum_ =  np.mean(list1)
print(sum_)
list_name = np.array(list_name).reshape(-1, 1)
list1 = np.array(list1).reshape(-1, 1)
need =  np.array(need).reshape(-1, 1)
data = np.concatenate((list_name,list1,need), axis = 1)
print(data.shape)

cols = ['words', 'number_samples', 'add_amounts']
df =  pd.DataFrame(data, columns=cols)

df.to_csv('distribute_data.csv', encoding='utf-8', index=False)


