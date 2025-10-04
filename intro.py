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
