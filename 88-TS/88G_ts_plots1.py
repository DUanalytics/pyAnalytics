#Topic: Time Series Plot
#-----------------------------
#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html

#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_csv('data/mtcars.csv')
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars

#%%%
import matplotlib.pyplot as plt
import datetime
import numpy as np

x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
x
y = np.random.randint(100, size=x.shape)
y
plt.plot(x,y)
plt.show();


# Using plotly.express
#https://plot.ly/python/time-series/
import plotly.express as px

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df.head()
px.line(df, x='Date', y='AAPL.High')
px.line?
%matplotlib inline
fig = px.line(df, x='Date', y='AAPL.High')
fig.show();

#
# Using graph_objects
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
fig.show();
