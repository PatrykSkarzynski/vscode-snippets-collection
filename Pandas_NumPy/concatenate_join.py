"""
|
| pandas.concat() allows to concatenate two or more DataFrames together but also joining them side-by-side
|
|
| ===========================
| =  ### CONCATENATING ###  =
| ===========================
|
| pass two DataFrames to concatenate them:
| -----------------------------------------
| pd.concat([df1, df2], axis = 0) # axis : {0/'index', 1/'columns'}, default 0 - The axis to concatenate along
|
| =====================
| =  ### JOINING ###  =
| =====================
|
| 
| pass two DataFrames to join them side-by-side:
| -----------------------------------------------
| pd.concat([df1, df2], axis = 1) # axis : {0/'index', 1/'columns'}, 1 - The axis to concatenate side-by-side
|
|
|
| df1.loc[[0], ['name']] # giving row and column as lists gives back DataFrame
| df1.loc[0, 'name'] # giving row and column NOT as lists gives back Series
|
| df1.loc[0:4, 'name':'protein'] # slicing first 5 rows and first 3 columns of the DataFrame
|
| df1.loc[[5, 8], 'name':'protein'] # indexing by 2 rows and slicing by 3 columns
| df1.loc[5:7, ['name', 'protein']] # indexing by 2 columns and slicing by 3 rows
|
| df1.iloc[9, 2] # giving 10th row and 3rd column NOT as lists gives back Series
| df1.iloc[[9], [2]] # giving 10th row and 3rd column as lists gives back DataFrame
|
| df1.iloc[0:5, 0:3] # slicing first 5 rows and first 3 columns of the DataFrame
|
| df1.iloc[[0, 2, 4], 0:3] # indexing by 3 rows and slicing by 3 columns
| df1.iloc[0:3, [0, 1, 2]] # indexing by 3 columns and slicing by 3 rows
|
| df1 = df1[0:5]
| df1.loc[6] = ['Trix', 110, 1, 25, 27.753301] # adding new row to the prepared DataFrame above
|
| df1.drop(2, axis = 0, inplace = True) # deleting row with label 2 and setting "inplace = True" to permanently delete row
| df1
|
|
| df1['My Column'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] # adding new column to the DataFrame
| df1
|
| df1.drop('My Column', axis = 1, inplace = True) # deleting column and setting "inplace = True" to permanently delete column
| df1
|
|
| df1.sort_values(by = 'calories') # sorting DataFrame numerically by 'calories' column
| df1.sort_values(by = 'name') # sorting DataFrame alphabetically by 'name' column
|
| df1.sort_values(by = 'calories', ascending = False) # sorting descending DataFrame numerically by 'calories' column
| df1.sort_values(by = 'name', ascending = False) # sorting descending DataFrame numerically by 'name' column
|
"""


import pandas as pd


# reading .csv file while using only name of the file which creates DataFrame1:
df1 = pd.read_csv('cereals1.csv')
df1

# reading .csv file while using only name of the file which creates DataFrame2:
df2 = pd.read_csv('cereals2.csv')
df2


# pass two DataFrames to concatenate them:
# -----------------------------------------
pd.concat([df1, df2], axis = 0) # axis : {0/'index', 1/'columns'}, default 0 - The axis to concatenate along

# pass two DataFrames to join them side-by-side:
# -----------------------------------------------
pd.concat([df1, df2], axis = 1) # axis : {0/'index', 1/'columns'}, 1 - The axis to concatenate side-by-side
