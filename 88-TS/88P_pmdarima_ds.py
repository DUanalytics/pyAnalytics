#Topic: Time Series - Data Sets
#-----------------------------
#libraries

import pmdarima as pm
###################################################################
# You can load the datasets via load_<name>
lynx = pm.datasets.load_lynx()
print("Lynx array:")
print(lynx)

# You can also get a series, if you rather
print("\nLynx series head:")
print(pm.datasets.load_lynx(as_series=True).head())

# Several other datasets:
air_passengers = pm.datasets.load_airpassengers()
air_passengers
austres = pm.datasets.load_austres()
austres
heart_rate = pm.datasets.load_heartrate()
heart_rate
wineind = pm.datasets.load_wineind()
wineind
woolyrnq = pm.datasets.load_woolyrnq()
woolyrnq

#%%%% 
import pmdarima.datasets as pm

#Air Passengers
#The classic Box & Jenkins airline data. Monthly totals of international airline passengers, 1949 to 1960.
pm.load_airpassengers(True).head()
#7.2. Austres
#Numbers (in thousands) of Australian residents measured quarterly from March 1971 to March 1994. The sample consists of 89 records on a quarterly basis.
pm.load_austres(True).head()
#Heartrate - The heart rate data records sample of heartrate data borrowed from an MIT database. The sample consists of 150 evenly spaced (0.5 seconds) heartrate measurements.
pm.load_heartrate(True).head()
pm.load_heartrate(True)
#Lynx dataset records the number of skins of predators (lynx) that were collected over many years by the Hudson’s Bay Company (1821 - 1934). It’s commonly used for time-series benchmarking (Brockwell and Davis - 1991) and is built into R. The dataset exhibits a clear 10-year cycle.
pm.load_lynx(as_series=True).head()
pm.load_lynx(as_series=True)
#Wineind -This time-series records total wine sales by Australian wine makers in bottles <= 1 litre between Jan 1980 – Aug 1994. This dataset is found in the R forecast package.
pm.load_wineind(as_series=True).head()
pm.load_wineind(as_series=True)
#Woolyrnq - A time-series that records the quarterly production (in tonnes) of woollen yarn in Australia between Mar 1965 and Sep 1994. This dataset is found in the R forecast package.
pm.load_woolyrnq(True).head()
pm.load_woolyrnq(as_series=True)
