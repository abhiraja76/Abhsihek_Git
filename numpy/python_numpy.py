import numpy as np
####Arrays in Numpy
"""
Array in Numpy is a table of elements (usually numbers) which contains all of the same type, 
indexed by a tuple of positive integers. 
In Numpy, number of dimensions of the array is called rank of the array.
A tuple of integers giving the size of the array along each dimension is known as shape of the array.
An array class in Numpy is called as ndarray. 
Elements in Numpy arrays are accessed by using square brackets and
can be initialized by using nested Python Lists.
"""
"""
Creating a Numpy Array---->>>
    Arrays in Numpy can be created by multiple ways
        1). With various number of Ranks
        2). Defining the size of the Array.
        3). Arrays can also be created with the use of various data types such as lists, tuples, etc. 
           The type of the resultant array is deduced from the type of the elements in the sequences.
"""
###create 1 rank array
arr = np.array([1, 2, 3])
print("1 rank array = {0}".format(arr))

###create 2 rank array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("2 rank array = {0}".format(arr))

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)