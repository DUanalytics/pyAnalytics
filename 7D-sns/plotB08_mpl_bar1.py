#
#-----------------------------
#%https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar
import matplotlib.pyplot as plt

#matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)[source]
plt.bar(x=[1,2,3], height=[10,20,30])
plt.bar(x=[1,2,3], height=[10,20,30], width=0.5)
plt.bar(x=[1,2,3], height=[10,20,30], width=0.5, align='edge')
plt.bar(x=[1,2,3], height=[10,20,30], width=0.5, align='edge', color=['r','g','b'])
plt.bar(x=[1,2,3], height=[10,20,30], width=0.5, align='edge', color=['y','g','b'], tick_label = ['A','B','C'] , edgecolor='r', linewidth=4)
plt.bar(x=[1,2,3], height=[10,20,30])
plt.barh(y=[1,2,3], width=[10,20,30])
