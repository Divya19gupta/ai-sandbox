import numpy as np
print("NumPy imported successfully!")


## INTRO:

print('Intro to NumPy')
print(np.array([1, 2, 3]))
print(np.zeros((2, 3))) #(2,3) shape of array, it fills the array with zeros as default value
print(np.ones((3, 2))) #(3,2) shape of array, it fills the array with ones as default value
print(np.full((2, 2), 7)) #(2,2) shape of array, it fills the array with specified value which is 7 here
print(np.arange(0, 10, 2)) #Creates an array with values from 0 to 10 with a step of 2 (start, stop, step)
print(np.eye(3)) #Creates a 3x3 identity matrix where one is on the diagonal and zeros elsewhere

## ARRAY PROPERTIES AND OPERATIONS:

print('Array Properties')
#Shape? Size? Type?
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) #Returns a tuple representing the dimensions of the array (rows * columns)
print(arr.size) #Returns the total number of elements in the array: rows * columns
print(arr.dtype) #Returns the data type of the elements in the array
print(arr.ndim) #Returns the number of dimensions (axes) of the array (2D, 3D, etc.)
print(arr.astype(np.str_)) #Converts the array to a different data type (here, to float64, np.int_) astype(new type)
#types: int, str, float64

#Operations:
print('Array Operations')
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

# arr = np.array([[1, 2, 3], [4, 5, 6]])
print('Array Indexing and Slicing')
print(arr[0, 1]) #Accesses the element at row 0, column 1
print(arr[:, 1]) #Accesses all rows in column 1
print(arr[1, :]) #Accesses all columns in row 1
# [start:stop (counts one before ):step]
print(arr[0:2, 1:3]) #Accesses a sub-array from row 0 to 1 and column 1 to 2
print(arr[-1])

print('Fancy Indexing') #helps in selecting non-sequential elements and do so by creating a copy of the data and does not change in the original array
print(arr[[0, 1], [1, 2]]) #Accesses elements at (0, 1) and (1, 2)

print('Boolean Masking/Filtering')
#It is used to filter elements based on conditions, creating a boolean array (True/False) that indicates which elements meet the criteria or simply returns the elements that meet the criteria.
print(arr[arr > 3]) #Accesses elements greater than 3
print(arr[arr % 2 == 0]) #Accesses even elements
print(arr[(arr > 2) & (arr < 6)]) #Accesses elements greater than 2 and less than 6
print(arr[(arr < 2) | (arr > 5)]) #Accesses elements less than 2 or greater than 5
print(~(arr > 3)) #Accesses elements not greater than 3
print(np.where(arr > 3, arr, 0)) #Replaces elements greater than 3 with their value, others with 0
print(np.where(arr % 2 == 0, arr, -1)) #Replaces even elements with their value, odd elements with -1

print('Reshaping, Resizing and Manipulating Arrays')
#Reshaping means to change the shape of an array without changing its data. Like convertng a 1D array to 2D or 3D.
#it never creates a copy of the data, it returns a new view of the original array with the specified shape.
print(arr.reshape(3, 2)) #Reshapes the array to 3 rows and 2 columns
print(arr.flatten()) #Flattens the array to 1D and returns a copy of the original array
print(arr.ravel()) #Returns a flattened array (1D view of the original array)

## ADVANCE TOPICS:

print('Advanced Topics')
#Adding/Removing Items: Original array remains unchanged, a new array is returned with the modifications.

arr2 = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])
print(np.insert(arr2, 1 , 3, axis=0)) #Inserts a row with value 3 at index 1 (axis=0 for row, axis=1 for column, axis=None for flattened array) 
print(np.insert(arr2, 0, [13, 14, 15], axis=1)) #Inserts a row at the end of the array
#NumPy doesn’t automatically interpret this as a column vector.
# Instead, it flattens it and tries to broadcast it across all rows, inserting each element sequentially into the flattened array along that axis.
# That’s why the data “wraps around” and ends up with one extra column’s worth of values at the end.

print(np.append(arr2, [[16, 17, 18]], axis=0)) #Appends a row at the end of the array
# print(np.append(arr2, [[16, 17, 18]], axis=1)) #Appends a column at the end of the array (1 row, 3 columns)
print(np.append(arr2, [[16], [17], [18]], axis=1)) #Appends a column at the end of the array (3 rows, 1 column)

arr1 = np.array([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
print(np.concatenate((arr2, arr1), axis=0)) #Concatenates a row at the end of the array
print(np.concatenate((arr2, arr1), axis=1))
print(np.delete(arr2, 1, axis=0)) #Deletes row at index 1
print(np.delete(arr2, 1, axis=1)) #Deletes column at index 1

#Stacking and Splitting Arrays:
print('Stacking and Splitting Arrays')

print(np.vstack((arr2, arr1))) #Vertically stacks two arrays (adds rows)
print(np.hstack((arr2, arr1))) #Horizontally stacks two arrays (adds columns)

print(np.split(arr2, 3, axis=0)) #Splits the array into 3 sub-arrays along rows
print(np.split(arr2, 3, axis=1)) #Splits the array into 3 sub-arrays along columns
print(np.hsplit(arr2, 3)) #Splits the array into 3 sub-arrays along columns
print(np.vsplit(arr2, 3)) #Splits the array into 3 sub-arrays along rows

#Broadcasting:
print('Broadcasting')

#So while using mathematical operations on arrays of different shapes, it is very difficult to perform element-wise operations directly using loops.
#So numpy helps in implementing these operations on all the elements of the arrays without using loops.


# In practice, these two always work together —
# 👉 Broadcasting makes shapes compatible,
# 👉 Vectorization performs the fast, elementwise math.
discount = 10 #10 percent discount
operation = arr - (arr * discount/100)
print(operation) #Applies a 10% discount to each element in the array arr

#Rule1: Matching Dimensions: If the arrays have the same shape, element-wise operations are performed directly.
#Rule2: Expanding Singleton Dimensions: If one array has a dimension of size 1, it is expanded to match the other array's size along that dimension. Ex: [1,2,3] + 10 = [11,12,13] 
#Rule3: Incompatible shaped: If the arrays have different shapes and is not a single element, a broadcasting error occurs. Ex: [1,2,3] + [1,2] => Error

diffarr = np.array([1, 2])
print(arr * 2) #Multiplies each element in arr by 2
print(arr + diffarr.reshape(2,1)) #Adds diffarr to each row of arr
# So, this shape is valid but the issue is that your diffarr only has 2 elements, and you tried to reshape it into (1, 3) (which needs 3 elements).
# Why (2,1) works?
# Along rows (axis 0): both have size 2 → ✅ fine.
# Along columns (axis 1): one has size 3, the other 1 → ✅ broadcast the single column to 3 columns.
# So NumPy internally expands diffarr like this:
# [[1],
#  [2]]
# →
# [[1, 1, 1],
#  [2, 2, 2]]

#Vectorization:
print('Vectorization')
#Applying operations to entire arrays without explicit loops, making code more concise and faster.

## HANDLING MISSING DATA:
print('Handling Missing Data')
# np.isnan: #Checks for NaN (Not a Number) values in an array, missing values and returns a boolean array
# np.nan_to_num: #Replace NaN with 0 and Inf with finite numbers
# np.isinf: #Checks for Inf (Infinity) values in an array

arr_with_nan = np.array([1, 2, np.nan, 4, np.inf, -np.inf]) #np.inf represents positive infinity 10 ^ 1000
print(np.isnan(arr_with_nan)) #Checks for NaN values
# You cannot compare NaN with anything, not even itself. So to check for NaN values, we use np.isnan() function.

np.set_printoptions(suppress=True) #Suppresses scientific notation for small numbers in NumPy print output
print(np.nan_to_num(arr_with_nan, nan=100, posinf=1000, neginf=-1000)) #Replaces NaN with 0 and Inf with a large finite number
print(np.isinf(arr_with_nan)) #Checks for Inf values


## DIFF BTW NUMPY AND PANDAS:

# NumPy handles numerical data efficiently using arrays (fast, low-level, homogeneous — all elements have the same type).
# Pandas builds on NumPy to handle labeled and tabular data using Series (1D) and DataFrames (2D) — great for data analysis with rows and columns, labels, and mixed data types.
# 👉 Use NumPy for math-heavy array operations.
# 👉 Use Pandas for structured data analysis and manipulation