#python : DUP - Topic :Encoding in Python
#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns


#type-1
# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)


#Type2
#https://www.analyticsvidhya.com/blog/2020/08/types-of-categorical-data-encoding
#pip install category_encoders
import category_encoders as ce
import pandas as pd
data=pd.DataFrame({'City':['Delhi', 'Mumbai', 'Hyderabad','Chennai', 'Bangalore','Delhi','Hyderabad']})

#Original Data
data

#encode the data
data_encoded=pd.get_dummies(data=data,drop_first=True)
data_encoded



#effect encoding
#This encoding technique is also known as Deviation Encoding or Sum Encoding. Effect encoding is almost similar to dummy encoding, with a little difference. In dummy coding, we use 0 and 1 to represent the data but in effect encoding, we use three values i.e. 1,0, and -1.
import category_encoders as ce
import pandas as pd
data=pd.DataFrame({'City':['Delhi','Mumbai','Hyderabad', 'Chennai','Bangalore', 'Delhi','Hyderabad']})
data
encoder=ce.sum_coding.SumEncoder(cols='City',verbose=False,)
encoder
#Original Data
data
encoder.fit_transform(data)

#hash
import category_encoders as ce
import pandas as pd

#Create the dataframe
data=pd.DataFrame({'Month':['January','April','March', 'April','Februay', 'June','July','June','September']})
data
#Create object for hash encoder
encoder=ce.HashingEncoder(cols='Month',n_components=6)
#Fit and Transform Data
encoder.fit_transform(data)

#binary
#Binary encoding is a combination of Hash encoding and one-hot encoding. In this encoding scheme, the categorical feature is first converted into numerical using an ordinal encoder. Then the numbers are transformed in the binary number. After that binary value is split into different columns.
#Binary encoding works really well when there are a high number of categories. For example the cities in a country where a company supplies its products.
#Import the libraries
import category_encoders as ce
import pandas as pd

#Create the Dataframe
data=pd.DataFrame({'city':['Delhi','Mumbai','Hyderabad','Chennai', 'Bangalore','Delhi', 'Hyderabad','Mumbai','Agra']})

#Create object for binary encoding
encoder= ce.BinaryEncoder(cols=['city'],return_df=True)

#Original Data
data
#Fit and Transform Data 
data_encoded=encoder.fit_transform(data) 
data_encoded


#BaseN
#In the numeral system, the Base or the radix is the number of digits or a combination of digits and letters used to represent the numbers. The most common base we use in our life is 10  or decimal system as here we use 10 unique digits i.e 0 to 9 to represent all the numbers. Another widely used system is binary i.e. the base is 2. It uses 0 and 1 i.e 2 digits to express all the numbers.
#For Binary encoding, the Base is 2 which means it converts the numerical values of a category into its respective Binary form. If you want to change the Base of encoding scheme you may use Base N encoder. In the case when categories are more and binary encoding is not able to handle the dimensionality then we can use a larger base such as 4 or 8.
#Import the libraries
import category_encoders as ce
import pandas as pd

#Create the dataframe
data=pd.DataFrame({'city':['Delhi','Mumbai', 'Hyderabad','Chennai', 'Bangalore', 'Delhi', 'Hyderabad','Mumbai','Agra']})

#Create an object for Base N Encoding
encoder= ce.BaseNEncoder(cols=['city'],return_df=True,base=5)

#Original Data
data
#Fit and Transform Data
data_encoded=encoder.fit_transform(data)
data_encoded


#target
#import the libraries
import pandas as pd
import category_encoders as ce

#Create the Dataframe
data=pd.DataFrame({'class':['A,','B','C','B','C','A','A','A'], 'Marks':[50,30,70,80,45,97,80,68]})
data
#Create target encoding object
encoder=ce.TargetEncoder(cols='class') 

#Original Data
data
#Fit and Transform Train Data
encoder.fit_transform(data['class'],data['Marks'])



#categorical colns
#https://pbpython.com/categorical-encoding.html
import pandas as pd
import numpy as np

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration", "num_doors", "body_style", "drive_wheels", "engine_location", "wheel_base", "length", "width", "height", "curb_weight","engine_type", "num_cylinders", "engine_size", "fuel_system", "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm","city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", header=None, names=headers, na_values="?" )
df.head()
df.dtypes
#focus on encoding the categorical variables, we are going to include only the object columns in our dataframe. Pandas has a helpful select_dtypes function which we can use to build a new dataframe containing only the object columns.
obj_df = df.select_dtypes(include=['object']).copy()
obj_df.head()
#couple of null values in the data that we need to clean up.
obj_df[obj_df.isnull().any(axis=1)]
obj_df["num_doors"].value_counts()
obj_df = obj_df.fillna({"num_doors": "four"})  #fill missing values

#approach1
obj_df["num_cylinders"].value_counts()

cleanup_nums = {"num_doors":  {"four": 4, "two": 2},  "num_cylinders" : {"four": 4, "six": 6, "five": 5, "eight": 8, "two": 2, "twelve": 12, "three":3 }}
obj_df = obj_df.replace(cleanup_nums)
obj_df.head()
#pandas “knows” the types of values in the columns so the object is now a int64
obj_df.dtypes


#approach2
#Another approach to encoding categorical values is to use a technique called label encoding. Label encoding is simply converting each value in a column to a number. For example, the body_style column contains 5 different values
#convertible -> 0, hardtop -> 1, hatchback -> 2, sedan -> 3, wagon -> 4

obj_df["body_style"] = obj_df["body_style"].astype('category')
obj_df.dtypes
obj_df["body_style_cat"] = obj_df["body_style"].cat.codes
obj_df.head()
#get the benefits of pandas categories (compact data size, ability to order, plotting support) but can easily be converted to numeric values for further analysis.


#Approach #3 - One Hot Encoding
#straightforward but it has the disadvantage that the numeric values can be “misinterpreted” by the algorithms. For example, the value of 0 is obviously less than the value of 4 but does that really correspond to the data set in real life? Does a wagon have “4X” more weight in our calculation than the convertible? 

pd.get_dummies(obj_df, columns=["drive_wheels"]).head()
#The new data set contains three new columns:
#drive_wheels_4wd, drive_wheels_rwd, drive_wheels_fwd

# function is powerful because you can pass as many category columns as you would like and choose how to label the columns using prefix . Proper naming will make the rest of the analysis just a little bit easier.

pd.get_dummies(obj_df, columns=["body_style", "drive_wheels"], prefix=["body", "drive"]).head()
#get_dummies returns the full dataframe so you will need to filter out the objects using select_dtypes when you are ready to do the final analysis.


#Approach #4 - Custom Binary Encoding
#here is a column called engine_type that contains several different values:

obj_df["engine_type"].value_counts()
#care about is whether or not the engine is an Overhead Cam (OHC) or not. In other words, the various versions of OHC are all the same for this analysis. If this is the case, then we could use the str accessor plus np.where to create a new column the indicates whether or not the car has an OHC engine.
obj_df["OHC_Code"] = np.where(obj_df["engine_type"].str.contains("ohc"), 1, 0)
obj_df[["make", "engine_type", "OHC_Code"]].head()


#%%%
#The previous version of this article used LabelEncoder and LabelBinarizer which are not the recommended approach for encoding categorical values. These encoders should only be used to encode the target values not the feature values.
from sklearn.preprocessing import OrdinalEncoder

ord_enc = OrdinalEncoder()
obj_df["make_code"] = ord_enc.fit_transform(obj_df[["make"]])
obj_df[["make", "make_code"]].head(11)


from sklearn.preprocessing import OneHotEncoder

oe_style = OneHotEncoder()
oe_results = oe_style.fit_transform(obj_df[["body_style"]])
pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_).head() #OrdinalEncoder and OneHotEncoder which is the correct approach to use for encoding target values.

obj_df = obj_df.join(pd.DataFrame(oe_results.toarray(), columns=oe_style.categories_))
obj_df


#adv appch
import category_encoders as ce

# Get a new clean dataframe
obj_df = df.select_dtypes(include=['object']).copy()

# Specify the columns to encode then fit and transform
encoder = ce.BackwardDifferenceEncoder(cols=["engine_type"])
encoder.fit_transform(obj_df, verbose=1).iloc[:,8:14].head()

encoder = ce.PolynomialEncoder(cols=["engine_type"])
encoder.fit_transform(obj_df, verbose=1).iloc[:,8:14].head()


#scikit-learn pipelines
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

# for the purposes of this analysis, only use a small subset of features

feature_cols = [ 'fuel_type', 'make', 'aspiration', 'highway_mpg', 'city_mpg','curb_weight', 'drive_wheels']

# Remove the empty price rows
df_ml = df.dropna(subset=['price'])

X = df_ml[feature_cols]
y = df_ml['price']

column_trans = make_column_transformer(( OneHotEncoder(handle_unknown= 'ignore'),  [ 'fuel_type', 'make', 'drive_wheels']),  (OrdinalEncoder(), ['aspiration']),  remainder='passthrough')

linreg = LinearRegression()
pipe = make_pipeline(column_trans, linreg)
cross_val_score(pipe, X, y, cv=10, scoring='neg_mean_absolute_error').mean().round(2)


#%%%summary
#Encoding categorical variables is an important step in the data science process. Because there are multiple approaches to encoding variables, it is important to understand the various options and how to implement them on your own data sets. The python data science ecosystem has many helpful approaches to handling these problems. I encourage you to keep these ideas in mind the next time you find yourself analyzing categorical variables. For more details on the code in this article, feel free to review the notebook.
