#Group by Dates
#-----------------------------
#%
#https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
import datetime

df = pd.DataFrame({'Branch': 'A A A A A A A B'.split(), 'Buyer': 'Carl Mark Carl Carl Joe Joe Joe Carl'.split(), 'Quantity': [1, 3, 5, 1, 8, 1, 9, 3], 'Date': [  datetime.datetime(2013, 1, 1, 13, 0), datetime.datetime( 2013, 1, 1, 13, 5), datetime.datetime(2013, 10, 1, 20, 0), datetime.datetime(2013, 10, 2, 10, 0), datetime.datetime(2013, 10, 1, 20, 0), datetime.datetime(2013, 10, 2, 10, 0), datetime.datetime(2013, 12, 2, 12, 0), datetime.datetime(2013, 12, 2, 14, 0)] })
df

#Groupby a specific column with the desired frequency. This is like resampling.
df.groupby([pd.Grouper(freq='1M', key='Date'), 'Buyer']).sum()


#
df = df.set_index('Date')
df['Date'] = df.index + pd.offsets.MonthEnd(2)
df.groupby([pd.Grouper(freq='6M', key='Date'), 'Buyer']).sum()

#
df = pd.DataFrame([[1, 2], [1, 4], [5, 6]], columns=['A', 'B'])
df
g = df.groupby('A')
g.tail(1)
g.nth(0)
g.nth(-1)
g.nth(0, dropna='any')  #not null item
g.nth(-1, dropna='any')  # NaNs denote group exhausted when using dropna 
#g.B.nth(0, dropna='all')



#
business_dates = pd.date_range(start='4/1/2014', end='6/30/2014', freq='B')

df = pd.DataFrame(1, index=business_dates, columns=['a', 'b'])
df
# get the first, 4th, and last date index for each month
df.groupby([df.index.year, df.index.month]).nth([0, 3, -1])


#
df = pd.DataFrame({'a': [1, 0, 0], 'b': [0, 1, 0], 'c': [1, 0, 0], 'd': [2, 3, 4]})
df.groupby(df.sum(), axis=1).sum()


#
dfg = pd.DataFrame({"A": [1, 1, 2, 3, 2], "B": list("aaaba")})
dfg
dfg.groupby(["A", "B"]).ngroup()
dfg.groupby(["A", [0, 0, 0, 1, 1]]).ngroup()


#
df = pd.DataFrame(np.random.randn(10, 2))
df
5//3, 6//3  #divisor
df.index // 5
df.groupby(df.index // 5).std()
