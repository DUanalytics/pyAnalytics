#Topic ----Plot Nine
#https://pypi.org/project/plotnine/
#installation of plotnine
# Using pip
# pip install plotnine         # 1. should be sufficient for most
# pip install 'plotnine[all]'  # 2. includes extra/optional packages
#https://plotnine.readthedocs.io/en/stable/installation.html
# Or using conda
# conda install -c conda-forge plotnine

import numpy as np
import pandas as pd
from plotnine import *
from plotnine.data import mtcars
#%%%
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + stat_smooth(method='lm')  + facet_wrap('~gear'))


#%%%
df = pd.DataFrame({   'variable': ['gender', 'gender', 'age', 'age', 'age', 'income', 'income', 'income', 'income'],    'category': ['Female', 'Male', '1-24', '25-54', '55+', 'Lo', 'Lo-Med', 'Med', 'High'],    'value': [60, 40, 50, 30, 20, 10, 25, 25, 40],})
df['variable'] = pd.Categorical(df['variable'], categories=['gender', 'age', 'income'])

df
(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_col() )

#%%
(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_col())


#%%%
(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_bar(stat='identity', position='dodge')) 

#%%
dodge_text = position_dodge(width=0.9)                              # new

(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_bar(stat='identity', position='dodge', show_legend=False)   + geom_text(aes(y=-.5, label='category'),                                      position=dodge_text, color='gray', size=8, angle=45, va='top') + lims(y=(-5, 60)))


#%%%
dodge_text = position_dodge(width=0.9)

(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_bar(stat='identity', position='dodge', show_legend=False) + geom_text(aes(y=-.5, label='category'),            position=dodge_text, color='gray', size=8, angle=45, va='top') + geom_text(aes(label='value'),position=dodge_text,size=8, va='bottom', format_string='{}%') + lims(y=(-5, 60)) )


#%%
dodge_text = position_dodge(width=0.9)
ccolor = '#555555'

(ggplot(df, aes(x='variable', y='value', fill='category')) + geom_bar(stat='identity', position='dodge', show_legend=False) + geom_text(aes(y=-.5, label='category'),             position=dodge_text, color=ccolor, size=8, angle=45, va='top')  + geom_text(aes(label='value'), position=dodge_text,size=8, va='bottom', format_string='{}%') + lims(y=(-5, 60)) + theme(panel_background=element_rect(fill='white'),            axis_title_y=element_blank(),  axis_line_x=element_line(color='black'), axis_line_y=element_blank(), axis_text_y=element_blank(),         axis_text_x=element_text(color=ccolor),  axis_ticks_major_y=element_blank(),         panel_grid=element_blank(),  panel_border=element_blank()))
