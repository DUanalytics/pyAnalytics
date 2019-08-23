#Facet Grid Plot
#-----------------------------
#%
import seaborn as sns
import matplotlib.cm as cm, matplotlib.font_manager as fm
import pandas as pd

df = pd.read_csv("data/rent_data.csv",parse_dates=[2])

sns.color_palette("bright")
sns.set(font_scale=1.5)
sns.set_style("white")
g=sns.FacetGrid(df, col="region", col_wrap=4,size=3, sharey=True ,aspect=1.2)
g.map(plt.plot, "week", "rent_per_sqft", color='k', marker='o', mfc='r',alpha=1)

g.set_xticklabels(rotation=90,fontsize=10)
g.set_titles("{col_name}")
g.set_xlabels("")
g.set_ylabels("")
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Avg. Rent/Sqft by Week', fontsize=30)

# g.map(plt.margins(0.05, 0.15))

#-------
from matplotlib import pyplot as plt
import matplotlib.cm as cm, matplotlib.font_manager as fm
import pandas as pd 
%matplotlib inline

#df = pd.read_csv("rent_data.csv",parse_dates=[2])

sns.color_palette("bright")
sns.set(font_scale=1.5)
sns.set_style("white")
g=sns.FacetGrid(df, col="region", col_wrap=4, height=3, sharey=True, aspect=1.2)
g.map(plt.plot, "week", "rent_per_sqft", color='k',   lw=1.25, marker='.',   mfc='r',  markevery=[0,-1],   ms=10)

for ax in g.axes:   ax.margins(0.05, 0.15)

g.set_xticklabels(rotation=90,fontsize=10)
g.set_titles("{col_name}")
g.set_xlabels("")
g.set_ylabels("")