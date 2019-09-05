#Topic ----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pydataset import data
#mtcars = data('mtcars')
#data=mtcars
#read data
path='e:/adata/xxxx.csv'
data = pd.read_csv(path)
data.head()
data.columns
data.dtypes
data.shape
#%%%



#%%%
transaction_df = pd.DataFrame({'Beer' : [1,0,1,0,1,0,0,1],  'Coke' : [0,1,1,0,1,0,0,1], 'Pepsi' : [1,0,0,1,0,0,1,0],   'Milk' : [0,1,0,1,1,1,0,1], 'Juice' : [0,0,1,0,0,1,1,1]})


#%%%
# calculate occurrence(support) for every product in all transactions
product_support_dict = {}
for column in transaction_df.columns:    product_support_dict[column] = sum(transaction_df[column]>0)
 
# visualise support
pd.Series(product_support_dict).plot(kind="bar")

# take data matrix from dataframe
transaction_matrix = transaction_df.as_matrix()
# get number of rows and columns
rows, columns = transaction_matrix.shape
# init new matrix
frequent_items_matrix = np.zeros((5,5))
# compare every product with every other
for this_column in range(0, columns-1):
    for next_column in range(this_column + 1, columns):
        # multiply product pair vectors
        product_vector = transaction_matrix[:,this_column] * transaction_matrix[:,next_column]
        # check the number of pair occurrences in baskets
        count_matches = sum((product_vector)>0)
        # save values to new matrix
        frequent_items_matrix[this_column,next_column] = count_matches
 
#print frequent_items_matrix
plot_matrix(frequent_items_matrix)

# and finally combine product names with data
frequent_items_df = pd.DataFrame(frequent_items_matrix, columns = transaction_df.columns.values, index = transaction_df.columns.values)
 
import seaborn as sns
# and plot
sns.heatmap(frequent_items_df)


# extract product pairs with minimum frequency(treshold) basket occurrences
def extract_pairs(treshold):
    output = {}
    # select indexes with larger or equal n
    matrix_coord_list = np.where(frequent_items_matrix >= treshold)
    # take values
    row_coords = matrix_coord_list[0]
    column_coords = matrix_coord_list[1]
    # generate pairs
    for index, value in enumerate(row_coords):
        #print index
        row = row_coords[index]
        column = column_coords[index]
        # get product names
        first_product = product_names[row]
        second_product = product_names[column]
        # number of basket matches
        matches = frequent_items_matrix[row,column]
        # put key values into dict
        output[first_product+"-"+second_product] = matches
 
    # return sorted dict
    sorted_output = OrderedDict(sorted(output.items(), key=lambda x: x[1]))
    return sorted_output
 
# plot pairs with minimum frequency of 1 basket matches
pd.Series(extract_pairs(1)).plot(kind="barh")