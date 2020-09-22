import os 

list_name = []
list1= []
for folder in os.listdir('SL-PTIT-50'):
    list1.append(len(os.listdir(os.path.join('SL-PTIT-50', folder))))
    list_name.append(folder)

list2= []
for folder in os.listdir('SL-PTIT-50-SENSOR'):
    list2.append(len(os.listdir(os.path.join('SL-PTIT-50-SENSOR', folder))))

for i,item in enumerate(list1):
    if list1[i] != list2[i]:
        print(list1[i])
        print(list_name[i])
        print(list2[i])

