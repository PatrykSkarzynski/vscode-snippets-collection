# Also describing how to operate on .csv with some Pandas methods

import pandas as pd


# reading .csv file while using only name of the file:
df = pd.read_csv('cereals1.csv')
df


def change_Index_With_PANDAS():
    """
    |
    | changing index column to picked existing column, which WON'T change original DataFrame:
    | ----------------------------------------------------------------------------------------
    | df.set_index('name')
    | 
    | changing index column to picked existing column, which WILL change original DataFrame:
    | ---------------------------------------------------------------------------------------
    | df.set_index('name', inplace = True)
    | df
    |
    """

def head_Tail_With_PANDAS():
    """
    |
    | head() gives first 5 rows of DataFrame/Series by DEFAULT:
    | ----------------------------------------------------------
    | df.head()
    |
    | pass desired number of rows as an argument to the function:
    | ------------------------------------------------------------
    | df.head(7)
    |
    | tail() gives last 5 rows of DataFrame/Series by DEFAULT:
    | ---------------------------------------------------------
    | df.tail()
    |
    | pass desired number of rows as an argument to the function:
    | ------------------------------------------------------------
    | df.tail(7)
    |
    """

def describe_With_PANDAS():
    """
    |
    | describe() gives quick statistical summary of each column of the DataFrame:
    | ----------------------------------------------------------------------------
    | df.describe()
    |
    """

class data_Operations_With_PANDAS():
    """
    |
    | ([]) brackets operator slices rows of the DataFrame and does NO change to the original DataFrame
    |
    | pass start index (inclusive) and an end index (exclusive) to the bracket operator to slice the rows of the DataFrame:
    | ----------------------------------------------------------------------------------------------------------------------
    | df[0:3]
    | df[1:4]
    |
    | 
    | modifying "df" variable to show desired amount of rows starting from desired row:
    | ----------------------------------------------------------------------------------
    | df = df[0:5]
    |
    """
    def columnIndexingWithPANDAS():
        """
        |
        | [] brackets operator allows also to index columns of the DataFrame:
        | -----------------------------------------------------------
        | | Indexing single column returns a Series,
        | | Indexing a list of columns returns DatFrame
        | 
        | pass labels of desired columns to the [] operator (NOT their position!):
        | -------------------------------------------------------------------------
        | df[['name']]
        | df[['name', 'rating']]
        |
        """
    def passingBooleanListWithPANDAS():
        """
        |
        | [] brackets operator allows also to get a list of booleans which get all the rows of the DataFrame for which the corresponding element is the list is True,
        |    and rows of the DataFrame for which the corresponding element in the list is False are ignored (this operator does NO change to the original DataFrame):
        |
        | pass a list of booleans to the [] operator, VisualStudioCode's Pandas sometimes require 10 booleans or less or more:
        | ---------------------------------------------------------------------------------------------------------------------
        | thirdRow = [False, False, True, False, False,
        |             False, False, False, False, False]
        | df[thirdRow]
        |
        """
    def filteringRowsWithPANDAS():
        """
        |
        | [] brackets operator allows also to apply conditions on one or more columns of the DataFrame and rows which satisfy those conditions are filtered out"
        |
        | pass desired row to be filtered:
        | ----------------------------------
        | condition = df['calories'] > 70
        | df[condition]
        | df[df['calories'] > 70]
        |
        |
        | [] brackets operator allows also to group conditions using and operator (&)
        |
        | pass desired rows to be filtered while using "&" operator:
        | -----------------------------------------------------------
        | df [ (df['calories'] > 70) & (df['protein'] < 4) ]
        |
        |
        | [] brackets operator allows also to group conditions while using the or (|) operator
        |
        | pass desired rows to be filtered while using "|" operator:
        | -----------------------------------------------------------
        | df[ (df['calories'] > 70) | (df['protein'] > 3) ]
        |
        """
    def locFilteringWithPANDAS():
        """
        |
        | loc[] method allows to index/slice a group of rows and columns based on their labels
        |
        |
        | ### INDEXING rows and columns ###
        |
        | pass row label and column label to index DataFrame:
        | ----------------------------------------------------
        | | df.loc[[0], ['name']] # giving row and column as lists gives back DataFrame
        | | df.loc[0, 'name'] # giving row and column NOT as lists gives back Series
        |
        |
        | ### SLICING rows and columns ###
        |
        | pass start index and an end index (BOTH inclusive) to the bracket operator to slice the rows of the DataFrame:
        | ---------------------------------------------------------------------------------------------------------------
        | df.loc[0:4, 'name':'protein'] # slicing first 5 rows and first 3 columns of the DataFrame
        |
        |
        | ### INDEXING AND SLICING rows and columns ###
        | 
        | pass start index as row labels to index DataFrame by rows and end index to the bracket operator to slice columns of the DataFrame:
        | -----------------------------------------------------------------------------------------------------------------------------------
        | df.loc[[5, 8], 'name':'protein'] # indexing by 2 rows and slicing by 3 columns
        | df.loc[5:7, ['name', 'protein']] # indexing by 2 columns and slicing by 3 rows
        |
        """
        class addingAndDeletingRowsWithLocPANDAS():
            def addingRowsWithLocPANDAS():
                '''
                |
                | loc[] method allows also to add more rows to the DataFrame, when row label does not exist,
                | a new row with the given label will be added at the end of the row
                |
                | pass not existing row label and data for it:
                | ---------------------------------------------
                | df = df[0:5]
                | df.loc[6] = ['Trix', 110, 1, 25, 27.753301] # adding new row to the prepared DataFrame above 
                |
                '''
            def deletingRowsWithLocPANDAS():
                '''
                |
                | loc[] method allows also to delete rows from DataFrame with drop() function, by specifying axis=0 for rows
                |
                | pass labels of the rows to be deleted:
                | ---------------------------------------
                | df.drop(2, axis = 0, inplace = True) # deleting row with label 2 and setting "inplace = True" to permanently delete row
                |
                '''
    def iloc_filtering_with_PANDAS():
        """
        |
        | iloc[] property allows to index/slice a group of rows and columns based on their positions (NOT labels)
        |
        |
        | ### INDEXING rows and columns ###
        |
        | pass row and column positions to index DataFrame:
        | --------------------------------------------------
        | df.iloc[9, 2] # giving 10th row and 3rd column NOT as lists gives back Series
        | df.iloc[[9], [2]] # giving 10th row and 3rd column as lists gives back DataFrame
        |
        |
        | ### SLICING rows and columns ###
        |
        | pass row and column positions (start index is inclusive but end idex is exclusive):
        | ------------------------------------------------------------------------------------
        | df.iloc[0:5, 0:3] # slicing first 5 rows and first 3 columns of the DataFrame
        |
        |
        | ### INDEXING AND SLICING rows and columns ###
        |
        | pass start index as row position to index DataFrame by rows and end index to the bracket operator to slice columns of the DataFrame:
        | -------------------------------------------------------------------------------------------------------------------------------------
        | df.iloc[[0, 2, 4], 0:3] # indexing by 3 rows and slicing by 3 columns
        | df.iloc[0:3, [0, 1, 2]] # indexing by 3 columns and slicing by 3 rows
        |
        """
    def addingColumnsWithPANDAS():
        """
        |
        | adding columns to the DataFrame using the same notation as adding a key-value pair to a dictionary,
        | if no column with the given name exists, a new column (with provided values) will be added to the DataFrame
        |
        | pass column name and list of values for that column:
        | -----------------------------------------------------
        | df['My Column'] = ['A', 'B', 'C', 'D', 'E'] # adding new column to the DataFrame
        |
        """
    def deletingColumnsWithPANDAS():
        """
        |
        | deleting columns of the DataFrame using drop() function by specifying axis=1 for columns
        |
        | pass column names to be deleted:
        | ---------------------------------
        | df.drop('My Column', axis = 1, inplace = True) # deleting column and setting "inplace = True" to permanently delete column
        |
        """
    def sorting_with_PANDAS():
        """
        |
        | sort_values() allows to sort the values in ascending order (by default) of a DataFrame with respect to a column:
        | -----------------------------------------------------------------------------------------------------------------
        | | If the values are words, they are sorted alphabetically
        | | If the values are numbers, they are sorted numerically
        |
        |
        | ### ASCENDING ###
        |
        | pass columns name to sort ascending DataFrame:
        | -----------------------------------------------
        | df.sort_values(by = 'calories') # sorting ascending DataFrame numerically by 'calories' column
        | df.sort_values(by = 'name') # sorting ascending DataFrame alphabetically by 'name' column
        |
        |
        | ### DESCENDING ###
        |
        | pass columns name to sort descending DataFrame:
        | ------------------------------------------------
        | df.sort_values(by = 'calories', ascending = False) # sorting descending DataFrame numerically by 'calories' column
        | df.sort_values(by = 'name', ascending = False) # sorting descending DataFrame numerically by 'name' column
        |
        """

def exporting_And_Saving_With_PANDAS():
    """
    |
    | to_csv() allows to export DataFrame as a .csv file:
    | ----------------------------------------------------
    | | If a file with specified filename exists, it will be modified
    | | If a file with specified filename doesn't exist, a new file with specified filename will be created 
    |
    | pass filename for the .csv file to be created:
    | -----------------------------------------------
    | df.to_csv('myFile1.csv', index_label = False) # exporting DataFrame to a new file without index column (index_label=False)
    | newDf = pd.read_csv('myFile1.csv')
    | newDf
    |
    | df.to_csv('myFile1.csv', index_label = True) # exporting DataFrame to a new file with index column (index_label=True)
    | newDf = pd.read_csv('myFile2.csv')
    | newDf
    |
    """

def concatenating_With_PANDAS():
    """
    |
    | pandas.concat() allows to concatenate two or more DataFrames together but also joining them side-by-side
    |
    |
    | ### CONCATENATING ###
    |
    | pass two DataFrames to concatenate them:
    | -----------------------------------------
    | pd.concat([df1, df2], axis = 0) # axis : {0/'index', 1/'columns'}, default 0 - The axis to concatenate along
    |
    |
    |
    | ### JOINING ###
    |
    | pass two DataFrames to join them side-by-side:
    | -----------------------------------------------
    | pd.concat([df1, df2], axis = 1) # axis : {0/'index', 1/'columns'}, 1 - The axis to concatenate side-by-side
    |
    """

def groupBy_With_Pandas():
    """
    |
    | groupby() allows to group DataFrame based in Series (the DataFrame is splitted into groups,
    |                                                      An aggregate function is applied to each column of the splitted DataFrame,
    |                                                      Results are combined together)
    |
    | pass column name based of which DataFrame will be grouped and use mean() to average it:
    | ----------------------------------------------------------------------------------------
    | df.groupby(df['Gender']).mean()
    |
    |
    |
    | Common aggregate functions in Pandas:
    | | mean() for average
    | | sum() for sum
    | | max() for maximum
    | | min() for minimum
    | | median() gives the median
    | | count() gives the total number of values
    | | std() is used for computing the standard deviation of a column
    |
    """



# df.loc[[0], ['name']] # giving row and column as lists gives back DataFrame
# df.loc[0, 'name'] # giving row and column NOT as lists gives back Series

# df.loc[0:4, 'name':'protein'] # slicing first 5 rows and first 3 columns of the DataFrame

# df.loc[[5, 8], 'name':'protein'] # indexing by 2 rows and slicing by 3 columns
# df.loc[5:7, ['name', 'protein']] # indexing by 2 columns and slicing by 3 rows

# df.iloc[9, 2] # giving 10th row and 3rd column NOT as lists gives back Series
# df.iloc[[9], [2]] # giving 10th row and 3rd column as lists gives back DataFrame

# df.iloc[0:5, 0:3] # slicing first 5 rows and first 3 columns of the DataFrame

# df.iloc[[0, 2, 4], 0:3] # indexing by 3 rows and slicing by 3 columns
# df.iloc[0:3, [0, 1, 2]] # indexing by 3 columns and slicing by 3 rows

# # df = df[0:5]
# df.loc[6] = ['Trix', 110, 1, 25, 27.753301] # adding new row to the prepared DataFrame above

# df.drop(2, axis = 0, inplace = True) # deleting row with label 2 and setting "inplace = True" to permanently delete row
# df


# df['My Column'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] # adding new column to the DataFrame
# df

# df.drop('My Column', axis = 1, inplace = True) # deleting column and setting "inplace = True" to permanently delete column
# df


# df.sort_values(by = 'calories') # sorting DataFrame numerically by 'calories' column
# df.sort_values(by = 'name') # sorting DataFrame alphabetically by 'name' column

# df.sort_values(by = 'calories', ascending = False) # sorting descending DataFrame numerically by 'calories' column
# df.sort_values(by = 'name', ascending = False) # sorting descending DataFrame numerically by 'name' column


# data = {'Gender': ['female', 'male', 'female', 'male'],
#         'Score': [85, 88, 95, 80]}
#
# df1 = pd.DataFrame.from_dict(data)
# df1
#
# df1.groupby(df1['Gender']).mean()