#numpy.zeros
#创建指定大小的数组，数组元素以 0 来填充：

#numpy.zeros(shape, dtype = float, order = 'C')
#参数说明：

#参数	描述
#shape	数组形状
#dtype	数据类型，可选
#order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组

import numpy as np
arr=np.zeros((8,8),dtype=int)
arr[0:-1:2,0:-1:2]=1
arr[1::2,1::2]=1
print(arr)