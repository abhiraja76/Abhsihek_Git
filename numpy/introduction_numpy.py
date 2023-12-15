"""
Numpy is a general-purpose array-processing package.
It provides a high-performance multidimensional array object, and tools for working with these arrays.
It is the fundamental package for scientific computing with Python.
Besides its obvious scientific uses,
Numpy can also be used as an efficient multi-dimensional container of generic data.
"""

"""
Arrays in NumPy
NumPy&#x2019s main object is the homogeneous multidimensional array.

It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
In NumPy, dimensions are called axes. The number of axes is rank.
NumPy&#x2019s array class is called ndarray. It is also known by the alias array.
"""
import numpy as np 
print("---------------------------------------------------------------")
# we are creating a two-dimensional array that has the rank of 2 as it has 2 axes. 
# The first axis(dimension) is of length 2, i.e., the number of rows, 
# and the second axis(dimension) is of length 3, i.e., the number of columns. 
# The overall shape of the array can be represented as (2, 3)

# Creating array object
arr = np.array([[1,2,3], 
                [4,2,5]])
print("type of array object = {0}".format(type(arr)))
print("array dimension(axes) = {0}".format(arr.ndim))
print("array shape = {0}".format(arr.shape))
print("array size = {0}".format(arr.size))
print("array element type = {0}".format(arr.dtype))
print("---------------------------------------------------------------")


