#python : DUP - Topic :.......
#https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550#:~:text=You%20can%20use%20the%20url,a%20url%20pandas%20can%20read.
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

import pandas as pd
sheet_id = "1XqOtPkiE_Q0dfGSoyxrH730RkwrTczcRbDeJJpqRByQ"
sheet_name = "sample_1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

print(url)

pd.read_csv(url)

