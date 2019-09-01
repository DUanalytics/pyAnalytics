#Rolling Mean
#-----------------------------
#%
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html

df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
df
df.rolling(2, win_type='triang').sum()
df.rolling(2).sum()

df.rolling(2, min_periods=1).sum()


#---
df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]}, index = [pd.Timestamp('20130101 09:00:00'), pd.Timestamp('20130101 09:00:02'), pd.Timestamp('20130101 09:00:03'), pd.Timestamp('20130101 09:00:05'), pd.Timestamp('20130101 09:00:06')])
df
df.rolling('2s').sum()
df.rolling('2s').mean()
