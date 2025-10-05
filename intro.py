import numpy as np

# Create a 2D numpy array
nparray = np.array([[10, 20, 30], [4, 5, 6]])

print(nparray)  # Print the array
print(nparray.shape)  # Print the shape of the array (rows, columns)
print(nparray.dtype)  # Print the data type of the array elements

# Create a 1D array of 10 zeroes (integer type)
withzeroes = np.zeros(10, dtype=int)
# Create a 1D array of 10 ones (integer type)
withones = np.ones(10, dtype=int)
# Create a 1D array of 5 uninitialized values (integer type)
withrandom = np.empty(5, dtype=int)

print(withzeroes)  # Print the array of zeroes
print(withones)  # Print the array of ones
print(withrandom)  # Print the uninitialized array (values may be random)

# Create an array with values from 2 to 8 (exclusive), with a step of 2
arr = np.arange(2, 9, 2)

# Create an array of 5 evenly spaced values between 0 and 10 (inclusive)
lin = np.linspace(0, 10, num=5)
print(arr)  # Print the array created with arange
print(lin)  # Print the array created with linspace
