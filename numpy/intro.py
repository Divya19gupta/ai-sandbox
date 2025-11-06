import numpy as np
print("NumPy imported successfully!")


## INTRO:

print(np.array([1, 2, 3]))
print(np.zeros((2, 3))) #(2,3) shape of array, it fills the array with zeros as default value
print(np.ones((3, 2))) #(3,2) shape of array, it fills the array with ones as default value
print(np.full((2, 2), 7)) #(2,2) shape of array, it fills the array with specified value which is 7 here
print(np.arange(0, 10, 2)) #Creates an array with values from 0 to 10 with a step of 2 (start, stop, step)
print(np.eye(3)) #Creates a 3x3 identity matrix where one is on the diagonal and zeros elsewhere

## ARRAY PROPERTIES AND OPERATIONS:

#Shape? Size? Type?
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) #Returns a tuple representing the dimensions of the array (rows * columns)
print(arr.size) #Returns the total number of elements in the array: rows * columns
print(arr.dtype) #Returns the data type of the elements in the array
print(arr.ndim) #Returns the number of dimensions (axes) of the array (2D, 3D, etc.)
print(arr.astype(np.str_)) #Converts the array to a different data type (here, to float64, np.int_) astype(new type)
#types: int, str, float64

#Operations:
print(arr + 10) #Adds 10 to each element in the array
print(arr * 2) #Multiplies each element in the array by 2
print(np.sqrt(arr)) #Calculates the square root of each element in the array
print(np.sum(arr)) #Calculates the sum of all elements in the array
print(np.mean(arr)) #Calculates the mean (average) of all elements in the array
print(np.max(arr)) #Finds the maximum value in the array
print(np.min(arr)) #Finds the minimum value in the array
print(np.std(arr)) #Calculates the standard deviation of the elements in the array
print(np.dot(arr, arr.T)) #Calculates the dot product of the array with its transpose
print(arr.T) #Transposes the array (swaps rows and columns)
print(np.var(arr)) #Calculates the variance of the elements in the array

#Indexing and Slicing: Picking single elements or sub-arrays vs selecting multiple elements or sub-arrays
#Fancy Indexing: Using arrays of indices to select multiple elements at once
#Boolean Masking: Using boolean arrays to filter elements based on conditions


## DIFF BTW NUMPY AND PANDAS:

# NumPy handles numerical data efficiently using arrays (fast, low-level, homogeneous — all elements have the same type).
# Pandas builds on NumPy to handle labeled and tabular data using Series (1D) and DataFrames (2D) — great for data analysis with rows and columns, labels, and mixed data types.
# 👉 Use NumPy for math-heavy array operations.
# 👉 Use Pandas for structured data analysis and manipulation