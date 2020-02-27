#numpy.put
#numpy.put(a, ind, v, mode='raise')[source]
#Replaces specified elements of an array with given values.

#The indexing works on the flattened target array. put is roughly equivalent to:

#a.flat[ind] = v
#Parameters:	
#a : ndarray
#Target array.

#ind : array_like
#Target indices, interpreted as integers.

#v : array_like
#Values to place in a at target indices. If v is shorter than ind it will be repeated as necessary.
#mode : {‘raise’, ‘wrap’, ‘clip’}, optional
#Specifies how out-of-bounds indices will behave.

#‘raise’ – raise an error (default)
#‘wrap’ – wrap around
#‘clip’ – clip to the range
#‘clip’ mode means that all indices that are too large are replaced by the index that addresses the last element along that axis. Note that this disables indexing with negative numbers.

#用法：np.random.choice(a, size=None, replace=True, p=None)
#返回：从一维array a 或 int 数字a 中，以概率p随机选取大小为size的数据，replace表示是否重用元素，即抽取出来的数据是否放回原数组中，默认为true（抽取出来的数据有重复）

import numpy as np 
n = 10
p = 3
Z = np.zeros((n,n))
print(f"init arr is \n{Z}")
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(f"random replace is \n{Z}")