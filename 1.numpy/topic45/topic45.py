#numpy.argmax(a, axis=None, out=None) 
#返回沿轴axis最大值的索引。

#Parameters: 
#a : array_like 
#数组 
#axis : int, 可选 
#默认情况下，索引的是平铺的数组，否则沿指定的轴。 
#out : array, 可选 
#如果提供，结果以合适的形状和类型被插入到此数组中。 
#Returns: 
#index_array : ndarray of ints 
#索引数组。它具有与a.shape相同的形状，其中axis被移除。 

import numpy as np 
arr=np.random.random(10)
print(f"random array is {arr}")
arr[arr.argmax()] = 0
print(f"replace the maximum value by 0 is {arr}")
