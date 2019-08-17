#Multiple Columns
#-----------------------------
#%
#Converting multiple columns to Categories

#multiple columns to categories
df=df2

df
for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes
df.dtypes



#plots
#https://realpython.com/python-matplotlib-guide/