#Topic: Process Mining
#-----------------------------
#libraries
#pip install pm4py
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.log.importer.xes import importer
from pm4py.visualization.petrinet import visualizer
log = importer.apply('data/running-example.xes')
log
net, initial_marking, final_marking = alpha_miner.apply(log)
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
gviz = visualizer.apply(net, initial_marking, final_marking)
visualizer.view(gviz)

#%%%
print(log[0])
log[0]
log[0][0]
#dictionary format

#%%
from pm4py.objects.log.importer.xes import importer as xes_importer
variant = xes_importer.Variants.ITERPARSE
parameters = {variant.value.Parameters.TIMESTAMP_SORT:True}
log = xes_importer.apply('data/running-example.xes', variant=variant, parameters=parameters)
log[0]
log[0][0]



#%% csv files
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
log_csv = pd.read_csv('data/running-example.csv', sep=';')
log_csv
log_csv = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
log_csv
log_csv.columns
log_csv.head()
log_csv = log_csv.sort_values('Timestamp')
log_csv.head()
log_csv.dtypes

import datetime
log_csv.head()
log_csv['Timestamp'] = pd.to_datetime(log_csv['Timestamp'], format='%d-%m-%Y:%H.%M')
log_csv

#%%generic event data manipulaton
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.util import func
log = xes_importer.apply('data/running-example.xes')
log = func.filter_(lambda t : len(t) > 2, log)
log
#event with trace less than 3

#%%%  Filtering event data
#filtering on timeframe
log_csv
log_csv.dtypes
from pm4py.algo.filtering.log.timestamp import timestamp_filter
log
#log object
filtered_log = timestamp_filter.filter_traces_contained(log, '2011-01-01 11:12:00', '2011-05-01 15:12:00')
filtered_log

#df object
log_csv.head()
df_timest_intersecting = timestamp_filter.filter_traces_intersecting(log_csv, '2010-01-23 00:00:00', '2011-01-23 00:00:00', parameters={timestamp_filter.Parameters.CASE_ID_KEY: "case:concept:name",timestamp_filter.Parameters.TIMESTAMP_KEY: "time:Timestamp" })
#error----

#log object - interesecting
filtered_log = timestamp_filter.filter_traces_intersecting(log, '2011-01-01 11:12:00', '2011-05-01 15:12:00')
filtered_log

#log object - apply
filtered_log_events = timestamp_filter.apply_events(log, '2011-01-01 11:12:00', '2011-05-01 15:12:00')
filtered_log_events

#log object - case performance
log_csv.sort_values(by=['Case ID','Timestamp'])
from pm4py.algo.filtering.log.cases import case_filter
filtered_log = case_filter.filter_case_performance(log, 100, 500000)
filtered_log


#start activities
from pm4py.algo.filtering.log.start_activities import start_activities_filter
log_start = start_activities_filter.get_start_activities(log)
log_start
filtered_log = start_activities_filter.apply(log, ['register request'])
filtered_log

log_af_sa = start_activities_filter.apply_auto_filter(log, parameters = {start_activities_filter.Parameters.DECREASING_FACTOR: 0.6})
log_af_sa

#end activities
from pm4py.algo.filtering.log.end_activities import end_activities_filter
log_end = end_activities_filter.get_end_activities(log)
log_end
filtered_log = end_activities_filter.apply(log, ['pay compensation', 'reject request'])
filtered_log

log_af_ea = end_activities_filter.apply_auto_filter(log, parameters = {end_activities_filter.Parameters.DECREASING_FACTOR: 0.6})
log_af_ea


#%%% Alpha Miner
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply('data/running-example.xes')
log

#apply alpha miner
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, intial_marking, final_marking = alpha_miner.apply(log)
net
initial_marking
final_marking

#visualise
from pm4py.visualization.petrinet import factory as pn_vis_factory
gviz = pn_vis_factory.apply(net, initial_marking, final_marking)
pn_vis_factory.view(gviz)
