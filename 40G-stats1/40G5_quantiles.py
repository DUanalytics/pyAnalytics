#Topic: Quantiles in
#-----------------------------
#libraries
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df=mtcars
df.quantile()
#0,100 ; #40,60
df.mpg.mean()
df.mpg.median()
df.mpg.sort_values()
df.quantile(q=.5) #default 50% Q2
df.quantile([0,.25, .50, .75, 1.0]) #quartiles:Q1, Q2, Q3, Q4
df.quantile(np.arange(0,1,.1))  #decile
np.arange(0,100,5)
df[['mpg','wt']].quantile(np.arange(0,1,.01))  #percentile
df[['cyl','gear','am']]= df[['cyl','gear','am']].astype('category')
df.quantile([.1,.5, .9], numeric_only=True, axis=0) #selected percentile
df.mpg.quantile([0,.25, .50,.6, .75, 1.0]) #numpy single column 
df["mpg"].plot.box()
#clockwise 
df["wt"].plot.box(vert=False)
df["wt"].plot.kde()


#Box Plots columns
fig = plt.figure(figsize=(10, 6))
plt.suptitle("Box Plots")
plt.subplot(2, 2, 1) # matrix of 2 x 2 plots : first plot
df["mpg"].plot.box() 
plt.title('Mileage')
plt.subplot(2, 2, 2) # matrix of 2 x 2 plots : 2nd plot
df.wt.plot.box() 
plt.title('Weight')
plt.subplot(2, 2, 3) # matrix of 2 x 2 plots : 3nd plot
df.hp.plot.box(vert=False)  #vert=False stands # for "no vertical"
plt.title('Horse Power')
plt.subplot(2, 2, 4) # matrix of 2 x 2 plots : 4th plot
df["disp"].plot.box() 
plt.title('Displacement')
plt.xticks(rotation=25)
plt.show();