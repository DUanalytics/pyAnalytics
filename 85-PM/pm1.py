#python : Topic : Process Mining in Python

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#other libraries
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.log.importer.xes import importer
from pm4py.visualization.petrinet import visualizer

#log data
#https://www.bupar.net/read_xes.html #https://bupar.net/eventdata/
url = 'https://pm4py.fit.fraunhofer.de/static/assets/examples/running-example.xes'
url
log = importer.apply('E:/data/pm/running-example.xes')
#logs stores as extension of list DS
#access can be done using index value
print(log[0]) #prints the first trace of the log
print(log[0][0]) #prints the first event of the first trace

#two ways of importing
#iterparse() and xml.etree 


#CSV files
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
pd.set_option('display.max_columns', 8)
log_csv = pd.read_csv('E:/data/pm/patients.csv', sep=',')
log_csv = dataframe_utils.convert_timestamp_columns_in_df( log_csv)
log_csv.dtypes
log_csv.columns
log_csv.head()
#patientNo will change (it is like rollno, customerid)
log_csv = log_csv.sort_values('time')
event_log = log_converter.apply(log_csv)
#error in setting up case ID
log_csv = pd.read_csv('E:/data/pm/patients.csv', sep=',')
log_csv.rename(columns = {'patient':'case:patient'}, inplace=True)
parameters = { log_converter.Variants.TO_EVENT_LOG.value.Parameters.CASE_ID_KEY:'case'}
event_log = log_converter.apply(log_csv, parameters= parameters, variant= log_converter.Variants.TO_EVENT_LOG)
log_csv.head()

#exporting to CSV
import pandas as pd
from pm4py.objects.conversion.log import converter as log_converter
dataframe = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)
dataframe.to_csv('E:/data/pm/exportFromLogs.csv')
