# -*- coding: utf-8 -*-
#Startup Options
#-----------------------------
#%
#https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
import pandas as pd

import seaborn as sns
# sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
iris.head()
iris
pd.options.display.max_rows
print(pd.options.display.max_rows)
pd.options.display.max_rows = 200
pd.options.display.max_rows
pd.options.display.max_columns
iris

pd.set_option('display.max_columns',None)


import pandas
#The API is composed of 5 relevant functions, available directly from the pandas namespace:
#
#get_option() / set_option() - get/set the value of a single option.
#reset_option() - reset one or more options to their default value.
#describe_option() - print the descriptions of one or more options.
#option_context() - execute a codeblock with a set of options that revert to prior settings after execution.
pd.set_option("display.max_rows", 101)
pd.get_option("display.max_rows")
#passing in a substring will work - as long as it is unambiguous:
pd.set_option("max_r", 102)
pd.get_option("display.max_rows")


#Reset options
pd.reset_option("^display")
pd.get_option("display.max_rows")



#Setting Startup Options in python/ipython Environmen
#Using startup scripts for the python/ipython environment to import pandas and set options makes working with pandas more efficient. To do this, create a .py or .ipy script in the startup directory of the desired profile. An example where the startup folder is in a default ipython profile can be found at:

#$IPYTHONDIR/profile_default/startup


#Frequently Used Options
df = pd.DataFrame(np.random.randn(7, 2))
pd.set_option('max_rows', 7)
df
pd.set_option('max_rows', 5)
df
#see ... 

#display.expand_frame_repr
#display.expand_frame_repr allows for the representation of dataframes to stretch across pages, wrapped over the full column vs row-wise.

df = pd.DataFrame(np.random.randn(5, 10))
pd.set_option('expand_frame_repr', True)
df
pd.set_option('expand_frame_repr', False)
df


#display.large_repr lets you select whether to display dataframes that exceed max_columns or max_rows as a truncated frame, or as a summary.
df = pd.DataFrame(np.random.randn(10, 10))
df
pd.set_option('max_rows', 5)
df
pd.set_option('large_repr', 'truncate')
df
pd.set_option('large_repr', 'info')
df
pd.reset_option('large_repr')
pd.reset_option('max_rows')


#display.max_colwidth sets the maximum width of columns. Cells of this length or longer will be truncated with an ellipsis.
df = pd.DataFrame(np.array([['foo', 'bar', 'bim', 'uncomfortably long string'] , ['horse', 'cow', 'banana', 'apple']]))
df
pd.set_option('max_colwidth', 40)
df
pd.set_option('max_colwidth', 6)
df
pd.reset_option('max_colwidth')


#display.max_info_columns sets a threshold for when by-column info will be given.
df = pd.DataFrame(np.random.randn(10, 10))
df
pd.set_option('max_info_columns', 11)
df.info()
pd.set_option('max_info_columns', 5)
df
pd.reset_option('max_info_columns')

#study more at https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html


#common options
mport pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df
