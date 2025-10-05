import numpy as np

# Create a 2D numpy array with one row
arr = np.array([[2, 1, 5, 3, 7, 4, 6, 8, 12, 14, 16, 11]])

# Sort the array along the last axis (row-wise)
arr = np.sort(arr)
print(arr)

# Create two 1D numpy arrays
x = np.array([1, 2, 5, 52])
y = np.array([20, 44])

# Concatenate the two arrays into one
result = np.concatenate((x, y))
print(result)

# Create a 3D numpy array
array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)

# Print the number of dimensions of the array
print("Dimension of the array is :", array_example.ndim)

# Print the shape of the array (dimensions and their sizes)
print("Shape of the array is :", array_example.shape)

# Print the total number of elements in the array
print("Size of the array is :", array_example.size)
