#numpy.bincount(x, weights=None, minlength=0)
#Count number of occurrences of each value in array of non-negative ints.

#The number of bins (of size 1) is one larger than the largest value in x. If minlength is specified, there will be at least this number of bins in the output array (though it will be longer if necessary, depending on the contents of x). Each bin gives the number of occurrences of its index value in x. If weights is specified the input array is weighted by it, i.e. if a value n is found at position i, out[n] += weight[i] instead of out[n] += 1.

#Parameters:	
#x : array_like, 1 dimension, nonnegative ints
#Input array.

#weights : array_like, optional
#Weights, array of the same shape as x.

#minlength : int, optional
#A minimum number of bins for the output array.

#New in version 1.6.0.

#Returns:	
#out : ndarray of ints
#The result of binning the input array. The length of out is equal to np.amax(x)+1.

#Raises:	
#ValueError
#If the input is not 1-dimensional, or contains elements with negative values, or if minlength is negative.

#TypeError
#If the type of the input is float or complex.

#每个bin给出了它的索引值在x中出现的次数

import numpy as np 

Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
print(f"random arr is {I}")
Z += np.bincount(I, minlength=len(Z))
print(Z)

# Another solution
# Author: Bartosz Telenczuk
#np.add.at(Z, I, 1)
#print(Z)