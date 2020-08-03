#Topic: Pie Plot
#-----------------------------
#libraries

import matplotlib.pyplot as plt

#structure
# my_data = [value1,value2,value3,...]
# my_labels = 'label1','label2','label3',...
# plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
# plt.title('My Title')
# plt.axis('equal')
# plt.show();

# my_data = [value1,value2,value3,...]
# my_labels = 'label1','label2','label3',...
# plt.pie(my_data,labels=my_labels,autopct='%1.1f%%')
# plt.title('My Title')
# plt.axis('equal')
# plt.show()


#%% List Data
Tasks = [300,500,700]

my_labels = 'Tasks Pending','Tasks Ongoing','Tasks Completed'
plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
plt.title('My Tasks')
plt.axis('equal')
plt.show();

#style - Start angle, Shadow, Colors, Explode component
Tasks = [300,500,700]

my_labels = 'Tasks Pending','Tasks Ongoing','Tasks Completed'
my_colors = ['lightblue','lightsteelblue','silver']
my_explode = (0, 0.1, 0)
plt.pie(Tasks, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow = True, colors= my_colors, explode=my_explode) #imp 
plt.title('My Tasks')
plt.axis('equal')
plt.show();



#%% pandas DF
from pandas import DataFrame #another way of importing

Data = {'Tasks': [300,500,700]}
df = DataFrame(Data,columns=['Tasks'])
print (df)


my_labels = 'Tasks Pending','Tasks Ongoing','Tasks Completed'
plt.pie(df,labels=my_labels,autopct='%1.1f%%')
plt.title('My Tasks')
plt.axis('equal')
plt.show();

my_labels = 'Tasks Pending','Tasks Ongoing','Tasks Completed'
my_colors = ['lightblue','lightsteelblue','silver']
my_explode = (0, 0.1, 0)
plt.pie(df, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode)
plt.title('My Tasks')
plt.axis('equal')
plt.show()