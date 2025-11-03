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

##Handling Missing Data:

- df.isnull(): Returns a table of boolean values indicating missing data by stating True for missing and False for non-missing values.
- df.isnull().sum(): Returns the count of missing values in each column.

#Removing/Replacing Missing Data:
- df.dropna(inplace=True): Removes rows and columns with missing data. If you add axis=1, it removes columns with missing data, otherwise it removes rows by default.

If the missing values are too frequent, it is better to replace them as it might cause loss of important data.

'''