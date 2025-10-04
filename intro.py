import numpy as np

nparray = np.array([[10, 20, 30], [4, 5, 6]])

print(nparray)
print(nparray.shape)
print(nparray.dtype)

withzeroes = np.zeros(10, dtype=int)
withones = np.ones(10, dtype=int)
withrandom = np.empty(5, dtype=int)

print(withzeroes)
print(withones)
print(withrandom)

# Create an array with values from 2 to 8 (exclusive), with a step of 2
arr = np.arange(2,9,2)

# Create an array of 5 evenly spaced values between 0 and 10 (inclusive)
lin = np.linspace(0, 10, num=5)
print(arr)
print(lin)