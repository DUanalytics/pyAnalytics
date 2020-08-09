#python : Topic : Process Mining in Python
#https://pm4py.fit.fraunhofer.de/documentation
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

#----------------------------------------------
#Event Data Manipulation
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.util import func

log = xes_importer.apply('E:/data/pm/running-example.xes')
log = func.filter_(lambda t: len(t) > 2, log)
log


#filtering event data
#logs type
from pm4py.algo.filtering.log.timestamp import timestamp_filter
filtered_log = timestamp_filter.filter_traces_contained  (log, "2011-03-09 00:00:00", "2012-01-18 23:59:59")
filtered_log

from pm4py.algo.filtering.log.timestamp import timestamp_filter
filtered_log = timestamp_filter.filter_traces_intersecting (log, "2011-03-09 00:00:00", "2012-01-18 23:59:59")
filtered_log

from pm4py.algo.filtering.log.cases import case_filter
filtered_log = case_filter.filter_case_performance(log, 86400, 864000)
filtered_log

#on DF
from pm4py.algo.filtering.pandas.timestamp import timestamp_filter

df_timest_intersecting = timestamp_filter.filter_traces_intersecting
(dataframe, "2011-03-09 00:00:00", "2012-01-18 23:59:59", parameters= {timestamp_filter.Parameters.CASE_ID_KEY: "case:concept:name", timestamp_filter.Parameters.TIMESTAMP_KEY: "time:timestamp"})




#Modeling
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join('E:/data/pm/running-example.xes'))

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
net, initial_marking, final_marking = alpha_miner.apply(log)
net
initial_marking
final_marking

import os
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner

log = xes_importer.apply(os.path.join('E:/data/pm/running-example.xes'))
net, initial_marking, final_marking = inductive_miner.apply(log)
net

from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.visualization.process_tree import visualizer as pt_visualizer

tree = inductive_miner.apply_tree(log)
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
import graphviz 
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)

#
from pm4py.objects.conversion.process_tree import converter as pt_converter
net, initial_marking, final_marking = pt_converter.apply(tree, variant=pt_converter.Variants.TO_PETRI_NET)


#heuristic Miner
from pm4py.objects.log.importer.xes import importer as xes_importer
import os
#log_path = os.path.join("tests", "compressed_input_data", "09_a32f0n00.xes.gz")
log_path = os.path.join('E:/data/pm/running-example.xes')
log = xes_importer.apply(log_path)

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
heu_net = heuristics_miner.apply_heu(log, parameters= {heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
gviz = hn_visualizer.apply(heu_net)
hn_visualizer.view(gviz)

#Petrinet
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
net, im, fm = heuristics_miner.apply(log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, im, fm)
pn_visualizer.view(gviz)

#DF graphs
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join('E:/data/pm/running-example.xes'))

from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
dfg = dfg_discovery.apply(log)

from pm4py.visualization.dfg import visualizer as dfg_visualization
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.FREQUENCY)
dfg_visualization.view(gviz)

#with performance
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization

dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE)
dfg_visualization.view(gviz)

#svg format
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.visualization.dfg import visualizer as dfg_visualization

dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
dfg_visualization.save(gviz, "dfg.svg")


#Conver DF graph to a workflow net
from pm4py.objects.log.importer.xes import importer as xes_importer

import os
filepath = os.path.join('E:/data/pm/running-example.xes')
log = xes_importer.apply(filepath)

from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
dfg = dfg_discovery.apply(log)

from pm4py.objects.conversion.dfg import converter as dfg_mining
net, im, fm = dfg_mining.apply(dfg)
net
im
fm


#Adding info about freq/ performance
from pm4py.visualization.petrinet import visualizer as pn_visualizer
parameters = {pn_visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=log)
pn_visualizer.save(gviz, "inductive_frequency.png")


#classifier
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
log = xes_importer.apply(filepath)
parameters = {alpha_miner.Variants.ALPHA_CLASSIC.value.Parameters.ACTIVITY_KEY: "concept:name"}
net, initial_marking, final_marking = alpha_miner.apply(log, parameters=parameters)

net
initial_marking
final_marking

#-----
import os
from pm4py.objects.log.importer.xes import importer as xes_importer

log = xes_importer.apply(filepath)
print(log.classifiers)

from pm4py.objects.log.util import insert_classifier
log, activity_key = insert_classifier.insert_activity_classifier_attribute(log, "Activity classifier")  #error

#------------
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
parameters = {alpha_miner.Variants.ALPHA_CLASSIC.value.Parameters.ACTIVITY_KEY: activity_key}
net, initial_marking, final_marking = alpha_miner.apply(log, parameters=parameters)
#error

import os
from pm4py.objects.log.importer.xes import importer as xes_importer

log = xes_importer.apply(filepath)
for trace in log:
 for event in trace:
  event["customClassifier"] = event["concept:name"] + event["lifecycle:transition"]

from pm4py.algo.discovery.alpha import algorithm as alpha_miner
parameters = {alpha_miner.Variants.ALPHA_CLASSIC.value.Parameters.ACTIVITY_KEY: "customClassifier"}
net, initial_marking, final_marking = alpha_miner.apply(log, parameters=parameters)

#Petrinet Management
import os
from pm4py.objects.petri.importer import importer as pnml_importer
net, initial_marking, final_marking = pnml_importer.apply(os.path.join("tests","input_data","running-example.pnml"))

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

from pm4py.objects.petri.exporter import exporter as pnml_exporter
pnml_exporter.apply(net, initial_marking, "petri.pnml")

pnml_exporter.apply(net, initial_marking, "petri_final.pnml", final_marking=final_marking)



#tree generation

from pm4py.simulation.tree_generator import simulator as tree_gen
parameters = {}
tree = tree_gen.apply(parameters=parameters)
from pm4py.objects.process_tree import semantics
log = semantics.generate_log(tree, no_traces=100)
from pm4py.objects.conversion.process_tree import converter as pt_converter
net, im, fm = pt_converter.apply(tree)

print(tree)
from pm4py.visualization.process_tree import visualizer as pt_visualizer
gviz = pt_visualizer.apply(tree, parameters= {pt_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT: "png"})
pt_visualizer.view(gviz)


#Decision Tree
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join("tests", "input_data", "roadtraffic50traces.xes"))

from pm4py.objects.log.util import get_log_representation
str_trace_attributes = []
str_event_attributes = ["concept:name"]
num_trace_attributes = []
num_event_attributes = ["amount"]
data, feature_names = get_log_representation.get_representation(log, str_trace_attributes, str_event_attributes, num_trace_attributes, num_event_attributes)  #error

data, feature_names = get_log_representation.get_default_representation(log)
import pandas as pd
dataframe = pd.DataFrame(data, columns=feature_names)
dataframe

dataframe.to_csv("features.csv", index=False)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(data, target)

from pm4py.visualization.decisiontree import visualizer as dectree_visualizer
gviz = dectree_visualizer.apply(clf, feature_names, classes)


#-----
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply(os.path.join("tests", "input_data", "roadtraffic50traces.xes"))

from pm4py.objects.log.util import get_log_representation
str_trace_attributes = []
str_event_attributes = ["concept:name"]
num_trace_attributes = []
num_event_attributes = ["amount"]

data, feature_names = get_log_representation.get_representation(log, str_trace_attributes, str_event_attributes, num_trace_attributes, num_event_attributes)

data, feature_names = get_log_representation.get_default_representation(log)

from pm4py.objects.log.util import get_class_representation
target, classes = get_class_representation.get_class_representation_by_trace_duration(log, 2 * 8640000)
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(data, target)

from pm4py.visualization.decisiontree import visualizer as dectree_visualizer
gviz = dectree_visualizer.apply(clf, feature_names, classes)

#%%% Statistics

from pm4py.statistics.traces.log import case_statistics
all_case_durations = case_statistics.get_all_casedurations(log, parameters={    case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"})

all_case_durations

from pm4py.statistics.traces.log import case_statistics
median_case_duration = case_statistics.get_median_caseduration(log, parameters={    case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"})
median_case_duration

#Case Arrival
from pm4py.statistics.traces.log import case_arrival
case_arrival_ratio = case_arrival.get_case_arrival_avg(log, parameters={    case_arrival.Parameters.TIMESTAMP_KEY: "time:timestamp"})
case_arrival_ratio

from pm4py.statistics.traces.log import case_arrival
case_dispersion_ratio = case_arrival.get_case_dispersion_avg(log, parameters={    case_arrival.Parameters.TIMESTAMP_KEY: "time:timestamp"})
case_dispersion_ratio


#Peformance Spectrum
from pm4py.statistics.performance_spectrum import algorithm as performance_spectrum
ps = performance_spectrum.apply(log, ["register request", "decide"], parameters= {performance_spectrum.Parameters.ACTIVITY_KEY: "concept:name", performance_spectrum.Parameters.TIMESTAMP_KEY: "time:timestamp"})
ps

#Business Hours
from pm4py.util.business_hours import BusinessHours
from datetime import datetime

st = datetime.fromtimestamp(100000000)
et = datetime.fromtimestamp(200000000)
bh_object = BusinessHours(st, et)
worked_time = bh_object.getseconds()
print(worked_time)

#Cycle Time and Waiting Time
from pm4py.objects.log.util import interval_lifecycle
enriched_log = interval_lifecycle.assign_lead_cycle_time(log)
#error


#display graphs
import os
from pm4py.objects.log.importer.xes import importer as xes_importer
log_path = os.path.join("tests","input_data","receipt.xes")
log = xes_importer.apply(log_path)

from pm4py.util import constants
from pm4py.statistics.traces.log import case_statistics
x, y = case_statistics.get_kde_caseduration(log, parameters={constants.PARAMETER_CONSTANT_TIMESTAMP_KEY: "time:timestamp"})

from pm4py.visualization.graphs import visualizer as graphs_visualizer

gviz = graphs_visualizer.apply_plot(x, y, variant=graphs_visualizer.Variants.CASES)
graphs_visualizer.view(gviz)

gviz = graphs_visualizer.apply_semilogx(x, y, variant=graphs_visualizer.Variants.CASES)
graphs_visualizer.view(gviz)
                                    