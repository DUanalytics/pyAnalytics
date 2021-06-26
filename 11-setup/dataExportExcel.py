#python : DUP - Topic : Python to Excel

https://www.geeksforgeeks.org/exporting-a-pandas-dataframe-to-an-excel-file/
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

  
# creating the DataFrame
marks_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12, 3: 13, 4: 67, 5: 89,  6: 90, 7: 56, 8: 34}, 'Name': {0: 'Ram', 1: 'Deep', 2: 'Yash', 3: 'Aman',4: 'Arjun', 5: 'Aditya', 6: 'Divya', 7: 'Chalsea', 8: 'Akash' }, 'Marks': {0: 89, 1: 97, 2: 45, 3: 78,  4: 56, 5: 76, 6: 100, 7: 87, 8: 81},'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C', 4: 'E', 5: 'C', 6: 'A', 7: 'B', 8: 'B'}})
marks_data  
# determining the name of the file
file_name = 'MarksData.xlsx'
  
# saving the excel
marks_data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

#
import pandas as pd
from pydataset import data
df = data('mtcars')
df.head()
file_name='mtcarsData.xlsx'
df.to_excel(file_name)
