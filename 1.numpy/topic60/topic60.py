#numpy.any
#numpy.any(a, axis=None, out=None, keepdims=<no value>)[source]
#Test whether any array element along a given axis evaluates to True.

#Returns single boolean unless axis is not None

#Parameters:	
#a : array_like
#Input array or object that can be converted to an array.

#axis : None or int or tuple of ints, optional
#Axis or axes along which a logical OR reduction is performed. The default (axis = None) is to perform a logical OR over all the dimensions of the input array. axis may be negative, in which case it counts from the last to the first axis.

#New in version 1.7.0.

#If this is a tuple of ints, a reduction is performed on multiple axes, instead of a single axis or all the axes as before.

#out : ndarray, optional
#Alternate output array in which to place the result. It must have the same shape as the expected output and its type is preserved (e.g., if it is of type float, then it will remain so, returning 1.0 for True and 0.0 for False, regardless of the type of a). See doc.ufuncs (Section “Output arguments”) for details.

#keepdims : bool, optional
#If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

#If the default value is passed, then keepdims will not be passed through to the any method of sub-classes of ndarray, however any non-default value will be. If the sub-class’ method does not implement keepdims any exceptions will be raised.

#Returns:	
#any : bool or ndarray
#A new boolean or ndarray is returned unless out is specified, in which case a reference to out is returned.

import numpy as np 

Z = np.random.randint(0,3,(3,10))
print(f"random is \n{Z}")
print((~Z.any(axis=0)).any())