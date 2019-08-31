#Seaborn  Label Plots
#-----------------------------
#%
#https://www.programcreek.com/python/example/96206/seaborn.barplot

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("tips")
groupedvalues=df.groupby('day').sum().reset_index()
groupedvalues
groupedvalues.iterrows() #method, no output
for row in groupedvalues.iterrows():    print(row)

pal = sns.color_palette("Greens_d", len(groupedvalues))
rank = groupedvalues["total_bill"].argsort().argsort() 
g=sns.barplot(x='day',y='tip',data=groupedvalues, palette=np.array(pal[::-1])[rank])

for index, row in groupedvalues.iterrows():
    g.text(row.name,row.tip, round(row.total_bill,2), color='black', ha="center")

plt.show()


#
from matplotlib import pyplot as plt
import numpy as np

def show_values_on_bars(axs):
    def _show_on_single_plot(ax):        
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height()
            value = '{:.2f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center") 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):      _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)

fig, ax = plt.subplots(1, 1)
g=sns.barplot(x='day',y='tip',data=groupedvalues, palette=np.array(pal[::-1])[rank])
show_values_on_bars(ax)
#https://stackoverflow.com/questions/43214978/seaborn-barplot-displaying-values

#
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/wesm/pydata-book/master/ch08/tips.csv", sep=',')
groupedvalues=df.groupby('day').sum().reset_index()
groupedvalues=groupedvalues.sort_values('total_bill').reset_index()
g=sns.barplot(x='day',y='tip',data=groupedvalues, palette="Blues")
