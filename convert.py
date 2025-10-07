import numpy as np

# Create a 1D numpy array
arr = np.array([1,2,3,4,5,6])
print(arr.shape)  # Prints the shape of the array (6,)

# Add a new axis to convert the 1D array to a 2D row vector
arr2 = arr[np.newaxis, :]
print(arr2.shape)  # Prints the shape of the new array (1, 6)

# Create a row vector by adding a new axis at the beginning
row_axis = arr[np.newaxis, :]

# Create a column vector by adding a new axis at the end
col_axis = arr[:, np.newaxis]

print(row_axis.shape)  # Prints (1, 6)
print(col_axis.shape)  # Prints (6, 1)

# Use np.expand_dims to add a new axis at position 1 (column vector)
arrr = np.expand_dims(arr, axis=1)
print(arrr)  # Prints the reshaped array as a column vector

# Use np.expand_dims to add a new axis at position 0 (row vector)
arr_3 = np.expand_dims(arr, axis=0)
print(arr_3)