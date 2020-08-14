#Topic ----Plot Nine- Bar Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#pip install plotnine --user
from plotnine import *
from plotnine.data import mpg
mpg.head()
#%%%
#geom_bar(mapping=None, data=None, stat='count', position='stack', na_rm=False,  inherit_aes=True, show_legend=None, width=None, **kwargs)

#%%%
mpg.columns
mpg.groupby('class').size()
ggplot(mpg) + geom_bar(aes(x='class'))


#%%%
ggplot(mpg) + geom_bar(aes(x='class', fill='drv'))

#%%
( ggplot(mpg) + geom_bar(aes(x='class', fill='drv')) + coord_flip() + theme_classic() )
