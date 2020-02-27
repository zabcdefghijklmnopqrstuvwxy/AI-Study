#numpy.ndenumerate(arr)[source]
#Multidimensional index iterator.

#Return an iterator yielding pairs of array coordinates and values.

#Parameters:	
#arr : ndarray
#Input array.

#numpy.ndindex(*shape)[source]
#An N-dimensional iterator object to index arrays.

#Given the shape of an array, an ndindex instance iterates over the N-dimensional index of the array. At each iteration a tuple of indices is returned, the last dimension is iterated over first.

#Parameters:	
#`*args` : ints
#The size of each dimension of the array.

import numpy as np 

Z = np.arange(9).reshape(3,3)
for index, value in np.ndenumerate(Z):
    print(f"index={index},value={value}")
for index in np.ndindex(Z.shape):
    print(f"index={index},Z[index]={Z[index]}")