#Topic: AR - transacation data
#-----------------------------
#libraries
from mlxtend.preprocessing import TransactionEncoder

dataset = [['Apple', 'Beer', 'Rice', 'Chicken'],
           ['Apple', 'Beer', 'Rice'],
           ['Apple', 'Beer'],
           ['Apple', 'Bananas'],
           ['Milk', 'Beer', 'Rice', 'Chicken'],
           ['Milk', 'Beer', 'Rice'],
           ['Milk', 'Beer'],
           ['Apple', 'Bananas']]

dataset
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
te_ary
#The NumPy array is boolean for the sake of memory efficiency when working with large datasets. If a classic integer representation is desired instead, we can just convert the array to the appropriate type
te_ary.astype("int")

#After fitting, the unique column names that correspond to the data array shown above can be accessed via the columns_ attribute:
te.columns_

f we desire, we can turn the one-hot encoded array back into a transaction list of lists via the inverse_transform function:

first4 = te_ary[:4]
te.inverse_transform(first4)
#[['Apple', 'Beer', 'Chicken', 'Rice'],['Apple', 'Beer', 'Rice'],['Apple', 'Beer'],['Apple', 'Bananas']]