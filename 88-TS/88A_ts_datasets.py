#Topic: Time Series - Data Sets
#-----------------------------
#libraries

import pmdarima as pm

# #############################################################################
# You can load the datasets via load_<name>
lynx = pm.datasets.load_lynx()
print("Lynx array:")
print(lynx)

# You can also get a series, if you rather
print("\nLynx series head:")
print(pm.datasets.load_lynx(as_series=True).head())

# Several other datasets:
air_passengers = pm.datasets.load_airpassengers()
austres = pm.datasets.load_austres()
heart_rate = pm.datasets.load_heartrate()
wineind = pm.datasets.load_wineind()
woolyrnq = pm.datasets.load_woolyrnq()