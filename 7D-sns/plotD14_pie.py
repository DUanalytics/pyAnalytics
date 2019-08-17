#Pie Chart
#-----------------------------
#%
import matplotlib.pyplot as plt

sizes=[40,30,30]
labels = ['BBA', 'MBA','PHD']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
ax1.axis('equal')
plt.show()


#%%%
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#909090'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12
labels = ['Male',  'Female']
percentages = [60, 40]
explode=(0.1,0)
#
color_palette_list = ['#009ACD', '#ADD8E6', '#63D1F4', '#0EBFE9', '#C1F0F6', '#0099CC']
fig, ax = plt.subplots()
ax.pie(percentages, explode=explode, labels=labels, colors= color_palette_list[0:2], autopct='%1.0f%%',  shadow=False, startangle=0,  pctdistance=1.2,labeldistance=1.4)
ax.axis('equal')
ax.set_title("Distribution of Gender in Class", y=.2)
ax.legend(frameon=False, bbox_to_anchor=(0.2,0.8))
plt.show()