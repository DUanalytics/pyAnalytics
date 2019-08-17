#Topic: Student Alcohol Consumption
#-----------------------------
#libraries
#https://github.com/akjadon/Python_ML_Practice_Solved/blob/master/pandas_exercises_solved/04_Apply/Students_Alcohol_Consumption/Exercises_with_solutions.ipynb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()

#slice columns
stud_alcoh = df.loc[: , "school":"guardian"]
stud_alcoh.head()

#lambda function
capitalizer = lambda x: x.capitalize()

stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

stud_alcoh.tail()

def majority(x):
    if x > 17:
        return True
    else:
        return False

stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()


def times10(x):
    if type(x) is int:
        return 10 * x
    return x
stud_alcoh.applymap(times10).head(10)
