#numpy.cumsum(a, axis=None, dtype=None, out=None)
#axis=0，按照行累加。
#axis=1，按照列累加。
#axis不给定具体值，就把numpy数组当成一个一维数组。
#不断累加即n0 n1 n2 使用cumsum变成 n0 n0+n1 n0+n1+n2

import numpy as np 

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

Z = np.arange(20)
print(moving_average(Z, n=3))