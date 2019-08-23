#json
#-----------------------------
#%
import json
path='/duwork/downloads/pydata/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
records=[json.loads(line) for line in open(path)]
records[0]['tz']
print(records[0]['tz'])
#time_zones=[rec['tz'] for rec in records]  # error
time_zones=[rec['tz'] for rec in records if 'tz' in rec]   #
time_zones[:10]
print(time_zones[:10])

# Counting
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] =1
    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts=defaultdict(int)
    for x in sequence:
        count[x] += 1
    return counts
counts= get_counts(time_zones)
print('Total Time Zones Cities', len(time_zones))
counts['America/New_York']

print('New York Count', counts['America/New_York'])

print('Sao Paulo Count', counts['America/Sao_Paulo'])

# Top Ten Time Zones and their count
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print("Top Ten TZ", top_counts(counts))






from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))



































# Counting Time zones with Pandas

from pandas import DataFrame, Series

frame = DataFrame(records)
print(frame)
print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])  # Frequency Table

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print("No Counts", tz_counts[:10])

import numpy as np
import matplotlib as plt

plt.interactive(True)

print("Drawing Plot")
tz_counts[:10].plot(kind='barh',rot=0)
plt.interactive(True)
plt.pyplot.show()
#plt.interactive(False)
#plt.pyplot.show()

print(frame['a'][1])
print(frame['a'][50])

import pandas
results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows','Not Windows')
print(operating_system[:15])
print(cframe['a'])

by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

# Sort in Ascending Order
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]
#count_subset = agg_counts.take(indexer)

import matplotlib
print(count_subset)
#print(matplotlib.get_backend())
#matplotlib.use('TkAgg')
#print(matplotlib.get_backend())
#plt.interactive(False) # Change to True
count_subset.plot(kind='barh',stacked=True)

import matplotlib.pyplot as p
p.plot(range(20),range(20))
p.show()
#Out[2]: [<matplotlib.lines.Line2D object at 0xa64932c>]

p.show()
#import matplotlib.pyplot as p
#vi /home/du/.local/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc

results = Series([x.split()[0] for x in frame.a.dropna()])
print('Results are ', results[:5])
print('Results are --', results.value_counts()[:8])

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Non Windows')
print(operating_system[:5])

