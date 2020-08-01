#Topic:
#-----------------------------
#libraries
import numpy as np
from scipy import stats
data = np.genfromtxt('E:/analytics/projects/pyanalytics/data/GDP_2018.csv', delimiter=',', usecols=[1,2], dtype=None, skip_header=1, skip_footer=1, encoding=None)

data

def find_max():
    h_item=0
    for item in data:
        if item[1] >= h_item:
            h_item = item[1]
            update_country = item[0].decode('UTF-8')
    print ('Max GDP is', h_item )
    print ('and country is ', update_country, '\n\n' )

find_max()

def find_min():
    h_item=999999

for item in data:
    if item[1] &lt;= h_item:
        h_item = item[1]
        update_country=item[0].decode(&#39;UTF-8&#39;)

  print (&quot;Min GDP is&quot;, h_item )
print ( &quot;and country is &quot;, update_country,&quot;\n\n &quot;)

find_min()

#Iterative Print
print (&quot;Printing Iteratively: &quot;)
for item in data:
print (item[0].decode(&#39;UTF-8&#39;), item[1])

##SUM
sum=0
for item in data:
sum=sum+item[1]
print (&quot;Total GDP for top 50 countries is &quot;, sum,&quot;\n\n&quot;)

#STATS
list_stat=[]
for item in data:
list_stat.append(item[1])
list_stat
list_stat
stats.describe(list_stat)
desc=stats.describe(list_stat)
print(&#39;Mean GDP is : %.2f&#39; % desc.mean, &quot;\n\n&quot;)
print(&#39;Standard Deviation is : %.2f&#39; % np.sqrt(desc.variance),&quot;\n\n&quot;)
print (&quot;Standaradised values of GDP are &quot;,(data_GDP-data_GDP.mean())/data_GDP.std())
#------------------
import numpy as np
from scipy import stats
data=np.genfromtxt(&#39;D:\\USB
Drive\HenryHarvin\Examples\GDP_2018.csv&#39;,delimiter=&#39;,&#39;,usecols=[1,2],dtype=None,skip_header=1,
skip_footer=1)
data_GDP=np.genfromtxt(&#39;D:\\USB
Drive\HenryHarvin\Examples\GDP_2018.csv&#39;,delimiter=&#39;,&#39;,usecols=2,dtype=None,skip_header=1,skip
_footer=1)

def find_max():
h_item=0
for item in data:
if item[1] &gt;= h_item:
h_item = item[1]
update_country= item[0].decode(&#39;UTF-8&#39;)
print (&quot;Max GDP is&quot;, h_item )
print (&quot;and country is &quot;, update_country, &quot;\n\n &quot; )

find_max()

def find_min():
h_item=999999

for item in data:
if item[1] &lt;= h_item:
h_item = item[1]
update_country=item[0].decode(&#39;UTF-8&#39;)
print (&quot;Min GDP is&quot;, h_item )
print ( &quot;and country is &quot;, update_country,&quot;\n\n &quot;)

find_min()

#Iterative Print
print (&quot;Printing Iteratively: &quot;)
for item in data:
print (item[0].decode(&#39;UTF-8&#39;), item[1])

##SUM
sum=0
for item in data:
sum=sum+item[1]
print (&quot;Total GDP for top 50 countries is &quot;, sum,&quot;\n\n&quot;)

#STATS
list_stat=[]
for item in data:
list_stat.append(item[1])
list_stat
list_stat
stats.describe(list_stat)
desc=stats.describe(list_stat)
print(&#39;Mean GDP is : %.2f&#39; % desc.mean, &quot;\n\n&quot;)
print(&#39;Standard Deviation is : %.2f&#39; % np.sqrt(desc.variance),&quot;\n\n&quot;)
print (&quot;Standaradised values of GDP are &quot;,(data_GDP-data_GDP.mean())/data_GDP.std())