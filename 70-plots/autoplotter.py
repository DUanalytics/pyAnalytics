#Topic:Auto Plotter
#-----------------------------
#https://pypi.org/project/autoplotter/
#https://analyticsindiamag.com/autoplotter-tutorial-open-source-python-library-for-gui-based-eda/

#libraries

#pip install autoplotter
import autoplotter
from autoplotter import run_app # Importing the autoplotter for GUI Based EDA

import plotly.express as px # Importing plotly express to load dataset
df = px.data.tips() # Getting the   Restaurant data

run_app(df) # Calling the autoplotter.run_app
