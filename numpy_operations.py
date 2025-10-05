import numpy as np

arr = np.array([[2, 1, 5, 3, 7, 4, 6, 8, 12, 14, 16, 11]])
arr = np.sort(arr)
print(arr)

x = np.array([1, 2, 5, 52])
y = np.array([20, 44])

result = np.concatenate((x, y))
print(result)

array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)

print("Dimension of the array is :", array_example.ndim)
print("Shape of the array is :", array_example.shape)
print("Size of the array is :", array_example.size)
