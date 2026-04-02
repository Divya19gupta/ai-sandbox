import pandas as pd

df = pd.read_csv('./data/students.csv') # read the data from csv file
print(df.head()) # print the first 5 rows of the data
print(df.info()) # print the info about the data like number of rows, columns, data types and memory usage
print(df.describe()) # print the statistical summary of the data

print(df.isnull())
print(df.isna())

print(df.isnull().sum()) # print the count of missing values in each column
print(df.isna().sum()) # print the count of missing values in each column