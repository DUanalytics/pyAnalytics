# -*- coding: utf-8 -*-
from io import StringIO  # got moved to io in python3.
import pandas as pd

import requests
r = requests.get('https://docs.google.com/spreadsheet/ccc?key=0Ak1ecr7i0wotdGJmTURJRnZLYlV3M2daNTRubTdwTXc&output=csv')
data = r.content
data

df = pd.read_csv(StringIO(data), index_col=0,parse_dates=['Quradate'])

df.head()



#%%
# Set first column as rownames in data frame

 


#%%  Not working
#pandas.Dataframe() but obviously needed to install and import gspread. And it worked fine!
#pip install gspread
import gspread as gs
gsheet = gs.open("https://docs.google.com/spreadsheets/d/1h7HU0X_Q4T5h5D1Q36qoK40Tplz94x_HZYHOJJC_edU")
Sheet_name ="slr1"
wsheet = gsheet.worksheet(Sheet_name)
dataframe = pd.DataFrame(wsheet.get_all_records())


#%%
#Derive the id from the google drive shareable link.
#For the file at hand the link is as below
#<https://drive.google.com/open?id=1-tjNjMP6w0RUV4GhJWw08ql3wYwsNU69>
file_id='1-tjNjMP6w0RUV4GhJWw08ql3wYwsNU69'
link='https://drive.google.com/uc?export=download&id={FILE_ID}'
csv_url=link.format(FILE_ID=file_id)
#The final url would be as below:-
#csv_url='https://drive.google.com/uc?export=download&id=1-tjNjMP6w0RUV4GhJWw08ql3wYwsNU69'
df = pd.read_csv(csv_url)
df


#%%
file_id='2023826519'
link='https://docs.google.com/spreadsheets/d/1h7HU0X_Q4T5h5D1Q36qoK40Tplz94x_HZYHOJJC_edU?export=download&id={FILE_ID}'
csv_url=link.format(FILE_ID=file_id)
url2 = 'https://docs.google.com/spreadsheets/d/1h7HU0X_Q4T5h5D1Q36qoK40Tplz94x_HZYHOJJC_edU/edit#gid=2023826519'
df2 = pd.read_csv(csv_url)
df2

#%%
def load_from_gspreadsheet(sheet_name, key):
    url = 'https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv&sheet={sheet_name}&headers=1'.format( key=key, sheet_name= sheet_name.replace(' ', '%20'))

#    log.info('Loading google spreadsheet from {}'.format(url))

    df = pd.read_csv(url)
    return df.drop([col for col in df.columns if col.startswith('Unnamed')], axis=1)

load_from_gspreadsheet('1h7HU0X_Q4T5h5D1Q36qoK40Tplz94x_HZYHOJJC_edU','2023826519')



#%%
#pip install pygsheets
import pygsheets
#pip install pygsheets # in anaconda prompt as admin
gc = pygsheets.authorize()

# Open spreadsheet and then workseet
sh = gc.open('my new ssheet')
wks = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
wks.update_cell('A1', "Hey yank this numpy array")

# update the sheet with array
wks.update_cells('A2', my_nparray.to_list())

# share the sheet with your friend
sh.share("myFriend@gmail.com")




#%%% https://pypi.org/project/gsheets/
pip install gsheets
from gsheets import Sheets
sheets
sheets['1X2AjCyh1Kcs-CA8ilGZyBZBobuFP7cSS9D-3a5LK6sk']
s = Sheets