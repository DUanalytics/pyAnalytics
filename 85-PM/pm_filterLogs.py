#python : Topic : PM - Logs
#https://pm4py.fit.fraunhofer.de/static/assets/api/1.3.4/_modules/index.html
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#http://pm4py.pads.rwth-aachen.de/documentation/filtering-logs/
#https://github.com/pm4py/pm4py-ws/tree/master/files/event_logs
#http://pm4py.pads.rwth-aachen.de/documentation/filtering-logs/
import os
from pm4py.objects.log.importer.xes import factory as xes_importer
os.path.join
log_path = os.path.join("E:\data","pm","receipt.xes")
log_path
log = xes_importer.import_log(log_path)

from pm4py.objects.log.util import sorting
log = sorting.sort_timestamp(log)

#Filtering on timeframe
from pm4py.algo.filtering.log.timestamp import timestamp_filter
filtered_log = timestamp_filter.filter_traces_contained(log, "2011-03-09 00:00:00", "2012-01-18 23:59:59")
print(len(log))
print(len(filtered_log))

from pm4py.algo.filtering.log.timestamp import timestamp_filter
filtered_log_events = timestamp_filter.apply_events(log, "2011-03-09 00:00:00", "2012-01-18 23:59:59")


print(sum([len(trace) for trace in filtered_log]))
print(sum([len(trace) for trace in filtered_log_events]))

#case performance
from pm4py.algo.filtering.log.cases import case_filter
filtered_log = case_filter.filter_on_case_performance(log, 86400, 864000)
filtered_log
print(len(filtered_log))

#start Activities
from pm4py.algo.filtering.log.start_activities import start_activities_filter

log_start = start_activities_filter.get_start_activities(log)
log_start
# dictionary reporting the start activities and the number of occurrences:
start_activities_filter.apply(log, ["Confirmation of receipt"])

#It is possible to keep automatically the most frequent start activities, using the apply_auto_filter function. The function accept as parameter a decreasingFactor (by default equal to 0.6),
from pm4py.algo.filtering.log.start_activities import start_activities_filter

log_af_sa = start_activities_filter.apply_auto_filter(log, parameters= {"decreasingFactor": 0.6})
print(start_activities_filter.get_start_activities(log_af_sa))

#end activities
from pm4py.algo.filtering.log.end_activities import end_activities_filter

log_end = end_activities_filter.get_end_activities(log)
log_end
end_activities_filter.apply(log, ["T05 Print and send confirmation of receipt", "T10 Determine necessity to stop indication"])

from pm4py.algo.filtering.log.start_activities import start_activities_filter

log_af_sa = start_activities_filter.apply_auto_filter(log, parameters={"decreasingFactor": 0.6})
print(start_activities_filter.get_start_activities(log_af_sa))

from pm4py.algo.filtering.log.end_activities import end_activities_filter
log_af_ea = end_activities_filter.apply_auto_filter(log, parameters={"decreasingFactor": 0.6})
print(end_activities_filter.get_end_activities(log_af_ea))

#traces
from pm4py.algo.filtering.log.variants import variants_filter
variants = variants_filter.get_variants(log)
variants

from pm4py.statistics.traces.log import case_statistics
variants_count = case_statistics.get_variant_statistics(log)
variants_count = sorted(variants_count, key=lambda x: x['count'], reverse=True)
print(variants_count)
print(len(variants_count))

#most common
filtered_log1 = variants_filter.apply(log, ["Confirmation of receipt,T02 Check confirmation of receipt,T04 Determine confirmation of receipt,T05 Print and send confirmation of receipt,T06 Determine necessity of stop advice,T10 Determine necessity to stop indication"])
filtered_log1
variants_count_filtered_log1 = case_statistics.get_variant_statistics(filtered_log1)
print(variants_count_filtered_log1)

#---
from pm4py.algo.filtering.log.attributes import attributes_filter
activities = attributes_filter.get_attribute_values(log, "concept:name")
resources = attributes_filter.get_attribute_values(log, "org:resource")
activities
resources

#not containing any resource
from pm4py.util import constants
tracefilter_log_pos = attributes_filter.apply(log, ["Resource10"], parameters= {constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY: "org:resource", "positive": True})
tracefilter_log_neg = attributes_filter.apply(log, ["Resource10"], parameters= {constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY: "org:resource", "positive": False})

eventsfilter_log = attributes_filter.apply_events(log, ["Resource10"], parameters= {constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY: "org:resource", "positive": True})
eventsfilter_log

from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.util import constants
filtered_log = attributes_filter.apply_auto_filter(log, parameters={ constants.PARAMETER_CONSTANT_ATTRIBUTE_KEY: "concept:name", "decreasingFactor": 0.6})
filtered_log


#filter on numeric attributes
import os
from pm4py.objects.log.importer.xes import factory as xes_importer

log = xes_importer.apply(os.path.join("tests", "input_data", "roadtraffic100traces.xes"))