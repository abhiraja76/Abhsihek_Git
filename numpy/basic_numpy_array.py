import numpy as np
# creating list 
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

# Create numpy array --> numpy.array(parameter)
arr = np.array([list_1, list_2, list_3])
print(arr)
print(type(arr))
print(arr.shape)
print(arr.size)

# numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object.
iterable = (a*a for a in range(8))
arr = np.fromiter(iterable, float)
 
print("fromiter() array :",arr)

#  numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.

# Example : numpy.arange([start, ]stop, [step, ]dtype=None)

arr = np.arange(1, 20 , 2,  dtype = np.float32)
print("arange array", arr)

#  numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. 
# Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

arr = np.linspace(5, 10, 4, dtype=np.int32)
print("linspace arr", arr)


#numpy.empty(): This function create a new array of given shape and type, without initializing value.

# Syntax: numpy.empty(shape, dtype=float, order=’C’)

print("empty arr = ", np.empty(5, dtype=np.int32))
print("empty arr = ", np.empty([2,5], dtype=np.int32))
print("empty arr = ", np.empty([3,5]))


# numpy.ones(): This function is used to get a new array of given shape and type, filled with ones(1).

# Syntax: numpy.ones(shape, dtype=None, order=’C’)
print("ones arr = ", np.ones([3,5]))
print("ones arr = ", np.ones([3,5], dtype=np.int64))

#  numpy.zeros(): This function is used to get a new array of given shape and type, filled with zeros(0). 

# Syntax: numpy.ones(shape, dtype=None)
print("zeros arr = ", np.zeros([3,5]))
