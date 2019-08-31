#Topic: Pandas - Merge  : Join DF
#-----------------------------
#libraries
#Inner Merge / Inner join – The default Pandas behaviour, only keep rows where the merge “on” value exists in both the left and right dataframes.
#Left Merge / Left outer join – (aka left merge or left join) Keep every row in the left dataframe. Where there are missing values of the “on” variable in the right dataframe, add empty / NaN values in the result.
#Right Merge / Right outer join – (aka right merge or right join) Keep every row in the right dataframe. Where there are missing values of the “on” variable in the left column, add empty / NaN values in the result.
#Outer Merge / Full outer join – A full outer join returns all the rows from the left dataframe, all the rows from the right dataframe, and matches up rows where possible, with NaNs elsewhere.
#The merge type to use is specified using the “how” parameter in the merge command, taking values “left”, “right”, “inner” (default), or “outer”
#on− Columns (names) to join on. Must be found in both the left and right DataFrame objects.
#how – type of join needs to be performed – ‘left’, ‘right’, ‘outer’, ‘inner’, Default is inner join
#Master Data
master = pd.DataFrame({'rollno':[1,2,3,4,5,7],"sname": ['Akhil', 'Avisha',"Kuntal","Guru","Narishma","Laxman"], "gender":['M',"F","M","M","M","M"]})
master
np.random.randint(50,80,4)
result = pd.DataFrame({'rollno':[1,2,3,4,6], 'subject1':np.random.randint(50,80,5), 'subject2':np.random.randint(55,75,5)})
result

#basic
summary1 = pd.merge(master, result)
summary
pd.merge(master, result, on='rollno')
pd.merge(master, result, on='rollno', how='left')

#specify options
summary2 = pd.merge(master, result, left_on='rollno', right_on='rollno')
summary2

#Left Join
summary3 = pd.merge(master, result, how='left')
summary3
#right join
summary4 = pd.merge(master, result, how='right')
summary4
#right with indicator : how joined
summary4b = pd.merge(master, result, how='right',indicator=True)
summary4b


#subset of columns
summary5 = pd.merge(master[['rollno','gender']], result[['rollno','subject1']], how='right')
summary5

#all 
summary6 = pd.merge(master, result, how='outer')
summary6
#common in both
summary7 = pd.merge(master, result, how='inner')
summary7


#Links
#https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
#http://www.datasciencemadesimple.com/join-merge-data-frames-pandas-python/