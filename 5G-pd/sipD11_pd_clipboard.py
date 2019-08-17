#Pandas - read / write to clipboard
#-----------------------------
#%
import pandas as pd
dfread = pd.read_clipboard()
dfread
#pandas.read_clipboard(sep='\\s+', **kwargs)[source]
dfread.to_clipboard()
dfread.iloc[2:4,1:3]
#now paste it in excel or csv
dfread.loc[2:4,['sub11','sub12']]



#when you want parse data
import pandas as pd
a   b           c       d
0   1           inf     1/1/00
2   7.389056099 N/A     5-Jan-13
4   54.59815003 nan     7/24/18
6   403.4287935 None    NaT

df = pd.read_clipboard(na_values=[None], parse_dates=['d'])
df
df.dtypes
