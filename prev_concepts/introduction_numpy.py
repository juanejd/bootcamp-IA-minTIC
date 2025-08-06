import numpy as np
import matplotlib.pyplot as plt

# matrix of zeros
array_zeros = np.zeros((2, 4))
print(array_zeros)
print("--------------------------------")

# matrix of ones
array_ones = np.ones((3, 3))
print(array_ones)
print("dimension in array_ones:", array_ones.shape)
print("# of dimensions in array_ones:", array_ones.ndim)
print("size in array_ones:", array_ones.size)

# matrix with value indicated
array_value = np.full((2, 3, 4), 8)
print(array_value)
print("---------------------")

# empty matrix saved in memory at the moment
array_empty = np.empty((1, 3, 9))
print(array_empty)
print("---------------------")

# array using list of python
array_list = np.array([[1, 2, 3], [4, 5, 6]])
print(array_list)
print("---------------------")

# array with a range (minimum, maximum, # of elements)
array_range = np.linspace(0, 6, 3)
print(array_range)
print("---------------------")

# array with random values (dimension, rows, columns)
array_random = np.random.rand(1, 10, 6)
print(array_random)
print("---------------------")

# histogram with random values
values = np.random.rand(1000)
plt.hist(values, 100)  # bins --> # of bars
plt.show()

# array with a function


def function(x, y):
    return x + 2 * y


array_function = np.fromfunction(function, (3, 3))
print(array_function)
print("---------------------")
