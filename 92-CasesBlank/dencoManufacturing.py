#Topic ---- Blank Case Study - Denco - Manufacturing Firm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%case details
#%%Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#Maximise revenue from high value parts
#%%Information Required
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#%%%
#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
#df = pd.read_csv('data/denco.csv')
df = pd.read_csv(url)


#%%%% : Summary1
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#count by customers, sort, pick top 5 
#Series

#%%% - Summary2
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#find total revenue of each customer, sort in descending.

#%%% Summary3
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#grouby partnum, find value of revenue, sell these more



#%%% Summary4
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#check for margin value, their individual margin and total sales margin like revenue


#%%% Extras
#Most sold items

#%%% Extras - Plan more



#end here
