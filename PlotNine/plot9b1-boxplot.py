#Topic ----Box Plot - Plot nine
#https://plotnine.readthedocs.io/en/latest/generated/plotnine.geoms.geom_boxplot.html#a-box-and-whiskers-plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import mtcars
#%%%
mtcars.columns
(ggplot(mtcars)    + geom_boxplot(aes(x='factor(gear)', y='mpg')))

#%%%
(ggplot(mtcars)    + geom_boxplot(aes(x='factor(gear)', y='mpg')) + facet_wrap('~cyl'))



#%%%
(ggplot(mtcars)    + geom_boxplot(aes(x='factor(gear)', y='mpg')) +  coord_flip())
