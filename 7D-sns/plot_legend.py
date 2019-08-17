#Plot - Legend
#-----------------------------
#%

#
#plt acts on the current axes. To get axes from a FacetGrid use fig. For example: 
g.fig.get_axes()[0].legend(loc='lower left')


#
import seaborn as sns
sns.set(style="whitegrid")

titanic = sns.load_dataset("titanic")

g = sns.factorplot("class", "survived", "sex",
                    data=titanic, kind="bar",
                    size=6, palette="muted",
                   legend_out=False)
g.despine(left=True)
g.set_ylabels("survival probability")

#
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



#https://stackoverflow.com/questions/27019079/move-seaborn-plot-legend-to-a-different-position
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import seaborn as sns
sns.set(style="ticks")

figure_name = 'rater_violinplot.png'
#figure_output_path = output_path + figure_name

viol_plot = sns.factorplot(x="Rater", 
                       y="Confidence", 
                       hue="Event Type", 
                       data=combo_df, 
                       palette="colorblind",
                       kind='violin',
                       size = 10,
                       aspect = 1.5,
                       legend=False)

viol_plot.ax.legend(loc=2)
#viol_plot.fig.savefig(figure_output_path)