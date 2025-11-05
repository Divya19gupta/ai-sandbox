import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}   
df = pd.DataFrame(data)     
print(df)

'''
## Basic Terms:

#Data Analysis: It means you are using pandas to analyze tabular data.
#Data Manipulation: You are creating and manipulating data
#Encoding errors: You are using pandas to handle data that may have encoding issues and to resolve it use utf-8 or latin1
#Series: A one-dimensional array-like object in pandas that can hold any data type.
#gcsfs: A library that allows pandas to read and write data directly from Google Cloud Storage.

## How to read and save data:

#Read data: read_csv/json.excel()
#Save data: to_csv/json/excel()
#Dataframe: A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
#Rows: df.head(), df.tail() tells the first and last 5/or add in value rows of the dataframe

#Methods:
#df.info(): Provides a concise summary of the DataFrame, including the index dtype and columns, non-null values and memory usage.
#df.describe(): Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
    - count: Number of non-null observations
    - mean: Mean of the values
    - std: Standard deviation of the values
    - min: Minimum value
    - 25%: First 25th percentile of the values which means median of the lower half of the data
    - 50%: Median or second quartile of the values which means middle value of the data
    - 75%: Third quartile of the values which means median of the upper half of the data
    - max: Maximum value

Before reading and manipulating data, its important to ask yourself these questions:
- How big your dataset is?
- What are the names of the Columns? By df.shape returns tuple (column,row) and df.columns

#Selecting and Filtering:
- df['Column_Name']: Select a single column
- df[['Col1', 'Col2']]: Select multiple columns
- df[df['Age'] > 25]: Filter rows based on a condition
- df[(df['Age'] > 25) &/| (df['City'] == 'New York')]: Filter rows based on multiple conditions

## Actually manipulating data:

#Adding Columns:
- df['New_Column'] = value or expression: (Add a new column to the DataFrame)
#Adding Column at precise location:
- df.insert(loc which is the index number, 'New_Column', value or expression): (Insert a new column at a specific location in the DataFrame)
#Accessing a particular cell and then modifying it:
- df.at[row_index, 'Column_Name not a new one'] = new_value: (Access and modify a specific cell in the DataFrame)
#Removing Columns:
- df.drop(columns=['Column_Name1','Column_Name2'], axis=1, inplace=True): (Remove a column from the DataFrame)
inplace=True means that the changes are done in original dataframe itself and false means that it returns a new dataframe with the changes.
axis=1 means we are dropping columns, axis=0 means we are dropping rows, but its not mentioned then by default its 0.

## Handling Missing Data:

#Checking for Missing Data:
- df.isnull(): Returns a table of boolean values indicating missing data by stating True for missing and False for non-missing values.
- df.isnull().sum(): Returns the count of missing values in each column.

#Removing/Replacing Missing Data:
- df.dropna(inplace=True): Removes rows and columns with missing data. If you add axis=1, it removes columns with missing data, otherwise it removes rows by default.
#If the missing values are too frequent, it is better to replace them as it might cause loss of important data.
- df.fillna(value, inplace=True): Replaces missing values with a specified value or you can even fill it with some calculated value like mean/median of that column.
- df['Column_Name'].fillna(df['Column_Name'].mean(), inplace=True): (Replace missing values in a specific column with the mean of that column)
#Interpolation:
It means filling in the missing values by estimation based on surrounding data points.
Ex: 10,20,NaN,40 can be filled as 10,20,30,40 by linear interpolation.
Linear - it assumes a straight line between known data points. Ex: 10,20,NaN,40 becomes 10,20,30,40
Polynomial - it fits a polynomial curve to the known data points. Ex: 10,20,NaN,40 can be filled as 10,20,35,40. It depends on the degree of the polynomial you choose. Here, a quadratic polynomial (degree 2) is used to estimate the missing value. It can be more than 2 but higher degrees can lead to overfitting. 
Time - it uses time-based methods to estimate missing values in time series data. Ex: If you have data for Jan, Feb, NaN, Apr, it can estimate the missing value for March based on trends from previous months. It is useful when dealing with time series data where the order of data points matters.

## Sorting and Aggregation:

#Sorting Data:
- df.sort_values(by=['Column_Name1','Column_Name2'], ascending=[True/False, True/False], inplace=True): Sorts the DataFrame based on the values in specific columns. True for ascending order, False for descending.
#Aggregation:
- df['Column_Name'].sum(): Calculates the sum of values in a specific column.
- df['Column_Name'].mean(): Calculates the mean of values in a specific column.
- df['Column_Name'].max(): Finds the maximum value in a specific column.
- df['Column_Name'].min(): Finds the minimum value in a specific column.
#Group By: 
You can split the data into groups and then apply some function on each group.
- df.groupby('Column_Name').agg({'Another_Column': 'sum/mean/max/min'}): Groups the DataFrame by a specific column and applies aggregation functions on other columns.
- df.groupby('Column_Name')['Another_Column' where we need to perform math calc].sum()/mean()/max()/min()/size()/std(): Another way to group by and aggregate.
- df.groupby(['Col1','Col2'])['Col3'].sum()/mean()/max()/min()/size()/std(): Group by multiple columns and calculate the mean of another column.

##Merging and Joining DataFrames:
# Merging DataFrames:
- pd.merge(df1, df2, on='Common_Column', how='inner/outer/left/right'): 

Example:
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'ID': [2, 4],
    'Age': [24, 22]
})

df1 = dataframe1
df2 = dataframe2
on = common column on which merging is done (basically unique key)
how = type of merge
    - inner: Returns only the rows with matching keys in both DataFrames. Ex: the result will have only IDs 2.
    - outer: Returns all rows from both DataFrames, filling in NaNs for missing matches. Ex: the result will have all the IDs (1,2,3,4) with NaN for 4 in df1 and NaN for 1,3 in df2. 
    - left: Returns all rows from the left DataFrame and matching rows from the right DataFrame. Ex: the result will have all IDs from df1 (1,2,3) with NaN for 4 in df2.
    - right: Returns all rows from the right DataFrame and matching rows from the left DataFrame. Ex: the result will have all IDs from df2 (2,4) with NaN for 1,3 in df1.
    - cross: Returns the Cartesian product of both DataFrames, such that each row from the first DataFrame is paired with every row from the second DataFrame. Ex: if df1 has 3 rows and df2 has 2 rows, the result will have 6 rows (3*2=6). The result returns 1,2,3 from df1 paired with 2,4 from df2 in all possible combinations.

# Concatenate DataFrames:
- pd.concat([df1, df2], axis=0/1, ignore_index=True): Concatenates two DataFrames either vertically (axis=0) or horizontally (axis=1). ignore_index=True resets the index in the resulting DataFrame.
    
'''