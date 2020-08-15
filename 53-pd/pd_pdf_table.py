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
df = read_pdf('data/mtcarsPDF.pdf')
read_pdf('data/mtcarsPDF.pdf', output_format='json')

from tabula import convert_into
convert_into('data/mtcarsPDF.pdf', 'mtcarsPDFCSV.csv', output_format='csv')
