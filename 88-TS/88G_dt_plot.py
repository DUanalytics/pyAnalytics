#Date Time - Generating Dates
#-----------------------------
#%

from datetime import datetime as dt
dir(dt)  #functions in dateime

import matplotlib.pyplot as plt
from matplotlib import dates as mdates  #import another date module
dir(mdates)  #functions in dates of mpl library

dt(2019,7,3)  #conversion to date; same as before

tempDates = [dt(2019,7,1), dt(2019,7,5), dt(2019,7,8), dt(2019,7,10)]
tempDates
type(tempDates)  #Individual dates
temp = [44, 42, 47, 40]

#plot date and temp
fig = plt.figure(dpi=128, figsize=(10,6))
#figure of certain size and resolution

plt.plot(tempDates, temp)
plt.plot(tempDates, temp, color='red')

#
plt.plot(tempDates, temp, color='red')
plt.title("Noida Temperatures in Jul 2019")
plt.ylabel("High Temperature Days")
x_axis = plt.axes().get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter("%d-%B"))
fig.autofmt_xdate()
plt.show()
#run above lines together
