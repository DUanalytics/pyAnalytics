#Merge in Python - Joining Data Frames
#-----------------------------
#%
!curl 'https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv'
import pandas as pd
pop = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv')
pop
areas = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv')
areas
abbrevs = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv')
abbrevs

pop.head()
areas.head()
abbrevs.head()

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged
merged.head()

merged.isnull().any()

merged[merged['population'].isnull()].head()
merged[merged['state'].isnull(), 'state/region'].unique()
merged.loc[merged['state/region']=='PR','state'] = 'Puerto Rico'

merged.loc[merged['state/region']=='USA','state'] = 'United States'
merged.isnull().any()

final = pd.merge(merged, areas, on='state', how='left')
final.head()
