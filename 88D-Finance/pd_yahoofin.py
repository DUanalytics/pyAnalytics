#Stock Prices
#-----------------------------
#%
#pip install pandas_datareader
#https://www.red-gate.com/simple-talk/sql/bi/historical-stock-prices-volumes-python-csv-file/
#%%%
#import external pandas_datareader library with alias of web
import pandas_datareader as web
 
#import datetime internal datetime module
#datetime is a Python module
import datetime
 
#datetime.datetime is a data type within the datetime module
start = datetime.datetime(2019, 6, 1)
end = datetime.datetime(2019, 6, 30)
 
#DataReader method name is case sensitive
sbi = web.DataReader("sbin.ns", 'yahoo', start, end)
sbi 
#invoke to_csv for df dataframe object from 
#DataReader method in the pandas_datareader library
sbi.to_csv('data/yahoo_sbi.csv')


#Populating a CSV File for a Watch List of Stock


#%%
#settings for importing built-in datetime and date libraries
#and external pandas_datareader libraries
 
import pandas_datareader.data as web
import datetime
 
#read ticker symbols from a file to python symbol list
symbol = []
with open('stocks/stocks.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close

#the start expression collects data that are up to five years old
 
end = datetime.datetime.today()
start = datetime.date(end.year,1,1)
end, start 
#set path for csv filec:/python_programs_output
path_out = 'stocks/'
 
#loop through n tickers in symbol list with i values of 0 through n
#if no historical data returned on any pass, try to get the ticker data again #for first ticker symbol write a fresh copy of csv file for historical data #on remaining ticker symbols append historical data to the file written for #the first ticker symbol and do not include a header row
 
i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out+'yahoo_stocks.csv')
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out+'yahoo_stocks.csv', mode = 'a', header=False)
            print (i, symbol[i],'has data stored to csv file')
    except:
        print("No information for ticker # and symbol:")
        print (i,symbol[i])
        continue
    i=i+1