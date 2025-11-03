import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}   
df = pd.DataFrame(data)     
print(df)

'''
# Data Analysis: It means you are using pandas to analyze tabular data.
# Data Manipulation: You are creating and manipulating data

#Encoding errors: You are using pandas to handle data that may have encoding issues and to resolve it use utf-8 or latin1
#Series: A one-dimensional array-like object in pandas that can hold any data type.
#gcsfs: A library that allows pandas to read and write data directly from Google Cloud Storage.
'''