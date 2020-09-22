import os
# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns


list_name = []
list1= []
for folder in os.listdir('SL-PTIT-50'):
    list1.append(len(os.listdir(os.path.join('SL-PTIT-50', folder))))
    list_name.append(folder)

# matplotlib histogram
fig, axes = plt.subplots()
plt.bar([i for i in range(1,51)],list1)

# Add labels
plt.title('Distribution of dataset')
plt.xlabel('Words')
plt.ylabel('Number samples')
plt.show()