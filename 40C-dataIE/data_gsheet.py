#Topic: Import from Google Sheet
#-----------------------------
#libraries
import pandas as pd

test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + '0Ak1ecr7i0wotdGJmTURJRnZLYlV3M2daNTRubTdwTXc' + '/export?gid=0&format=csv',                index_col=0, parse_dates=['Quradate']      )
test.head(5) 
