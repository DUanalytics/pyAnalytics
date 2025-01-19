#Topic: Import from Google Sheet
#-----------------------------
#libraries
import pandas as pd

test = pd.read_csv('https://docs.google.com/spreadsheets/d/' + '0Ak1ecr7i0wotdGJmTURJRnZLYlV3M2daNTRubTdwTXc' + '/export?gid=0&format=csv',                index_col=0, parse_dates=['Quradate']      )
test.head(5) 

test = pd.read_csv('https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk' + '/export?gid=1858159025&format=csv',  index_col=0 )
test.head(5)
test.shape
type(test)



test = pd.read_csv('https://docs.google.com/spreadsheets/d/1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk' + '/export?gid=0&format=csv',  index_col=0 )
test.head(5)
test.shape
type(test)

