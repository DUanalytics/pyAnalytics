#Topic:US Crime
#-----------------------------
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()

crime.info()

# pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()

crime = crime.set_index('Year', drop = True)
crime.head()

del crime['Total']
crime.head()

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

crimes

#dangerous decade to live
# apparently the 90s was a pretty dangerous time in the US
crime.idxmax(0)
#year in which max of each column had
