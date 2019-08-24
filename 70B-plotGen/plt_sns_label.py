#Seaborn - Label Points
#-----------------------------
#%https://stackoverflow.com/questions/45849028/seaborn-facetgrid-pointplot-label-data-points
import matplotlib.pyplot as plt
import seaborn as sns

#
attend = sns.load_dataset("attention")
attend.head(3)
#
sns.set_style("whitegrid", {'axes.grid' : False, 'axes.edgecolor': 'none'})
g = sns.FacetGrid(attend, col="subject", col_wrap=5, height=1.5, ylim=(0, 10))

def f(x,y, **kwargs):
    ax = sns.pointplot(x,y,**kwargs)
    ax.axhline(5, alpha=0.5, color='grey')
    for i in range(len(x)):
        ax.annotate(str(y.values[i]), xy=(x.values[i]-1, y.values[i]), fontsize=8, xytext = (0,10), textcoords="offset points", color=kwargs.get("color","k"), bbox=dict(pad=.9,alpha=0.2, fc='limegreen' , color='none'), va='center', ha='center', weight='bold')

g.map(f, "solutions", "score", scale=.7)
plt.show();
