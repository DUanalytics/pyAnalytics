#TS - Case
#-----------------------------
#%


#dataset
url= 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-total-female-births.csv'
#https://machinelearningmastery.com/load-explore-time-series-data-python/
series = pd.read_csv(url, squeeze=True)
#squeeze=True: We hint that we only have one data column and that we are interested in a Series and not a DataFram
series.head()
series.describe()
#
tsdata = series.copy()
tsdata.set_index('Date', inplace=True)
tsdata.head()
#
tsdata.index
tsdata.resample('W')


resample() method, which splits the DatetimeIndex into time bins and groups the data by time bin