#Topic ----Plot Nine- Bar Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#pip install plotnine --user
from plotnine import *

#https://datacarpentry.org/python-ecology-lesson/07-visualization-ggplot-python/index.html


from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars
mtcars
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + stat_smooth(method='lm') + facet_wrap('~gear'))

ggplot(mtcars, aes('wt', 'hp', color='factor(cyl)')) + geom_point(aes(size='mpg')) + labs(title='MT cars', subtitle ='wt vs hp', x='weight', y='horsepower') + geom_text(aes(label='name'))


#%%%
%matplotlib inline
import plotnine as p9
from plotnine.data import mtcars
from adjustText import adjust_text
#https://github.com/Phlya/adjustText/wiki
p9.ggplot(mtcars, aes('wt', 'hp', color='factor(cyl)')) + p9.geom_point(aes(size='mpg')) + p9.labs(title='MT cars', subtitle ='wt vs hp', x='weight', y='horsepower') + p9.geom_text(aes(label='name'), size=11, nudge_y=2)
p9.geom_text?
plt.ioff()# and plt.ion()
plt.close()
%matplotlib
