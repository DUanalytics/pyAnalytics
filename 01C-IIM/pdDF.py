#Topic:Create DF
#-----------------------------
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pandas data frame - multi column
#first create two series
course = pd.Series(['BTech','MTech','BBA','MBA'])
strength = pd.Series([100, 50, 200, 75])
fees = pd.Series([2.5, 3, 2, 4])
course, strength, fees
pd1 = pd.DataFrame([course, strength,fees])
pd1  #not the correct method of DF  # tranposed

#better way
pd2 = pd.DataFrame({'course':course, 'strength':strength, 'fees':fees})
#count ?
pd2 #better way
pd2.index
pd2.columns
pd2.values
