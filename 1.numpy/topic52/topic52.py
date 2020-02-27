#numpy.atleast_2d(*arys)[source]
#View inputs as arrays with at least two dimensions.

#Parameters:	
#arys1, arys2, … : array_like
#One or more array-like sequences. Non-array inputs are converted to arrays. Arrays that already have two or more dimensions are preserved.

#Returns:	
#res, res2, … : ndarray
#An array, or list of arrays, each with a.ndim >= 2. Copies are avoided where possible, and views with two or more dimensions are returned.

import numpy as np 

Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)

