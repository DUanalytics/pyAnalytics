#python : Topic : Table in PDFs to DF
#https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns

#pip install tabula-py
from tabula import read_pdf
read_pdf?
df = read_pdf('data/mtcarsPDF.pdf', pages='all')
df
read_pdf('data/mtcarsPDF.pdf', output_format='json', pages='all')

from tabula import convert_into
convert_into('data/mtcarsPDF.pdf', 'mtcarsPDFCSV.csv', output_format='csv', pages=1)

convert_into_by_batch('data', output_format='csv', pages='all')


#%%% not working
#pip install camelot-py[cv]
#pip install ghostscript
import camelot
import ghostscript
#https://www.ghostscript.com/download/gsdnld.html
camelot.read_pdf?
tables = camelot.read_pdf(filepath='data/mtcarsPDF.pdf', pages='1')
tables
#Please make sure that Ghostscript is installed
tables.n
tables[0].df

tables[0].to_csv('data/camelot.csv')
tables.export('data/camelot2.csv', f='csv', compress= True)



pip install setuptools#
