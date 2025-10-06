import numpy as np  # Import the numpy library

"""
This script demonstrates how to reshape 1D numpy arrays into 2D matrices using the `reshape` method.

Steps:
1. Creates a 1D numpy array with 6 elements and reshapes it into a 2x3 matrix (2 rows, 3 columns) using default row-major (C-style) order.
2. Creates another 1D numpy array with 9 elements and reshapes it into a 3x3 matrix using column-major (Fortran-style) order.
    # The 'order' parameter in reshape specifies the reading order of elements:
    # - 'C' (default): Row-major order (C-style)
    # - 'F': Column-major order (Fortran-style)

Outputs:
- Prints the reshaped arrays to the console.
"""

# Create a 1D numpy array with 6 elements
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2x3 matrix (2 rows, 3 columns)
reshaped = arr.reshape(2, 3)

print(reshaped)  # Print the reshaped array

# Create another 1D numpy array with 9 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Reshape the array into a 3x3 matrix using column-major (Fortran-style) order
reshaped = arr.reshape((3, 3), order="F")

print(reshaped)  # Print the reshaped array
