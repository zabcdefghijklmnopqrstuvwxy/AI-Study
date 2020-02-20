#numpy.diag(v,k=0) 官方文档
#以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转换成方阵（非对角线元素为0）.
#两种功能角色转变取决于输入的v。1

#参数详解：
#v : array_like.
#如果v是2D数组，返回k位置的对角线。

#如果v是1D数组，返回一个v作为k位置对角线的2维数组。

#k : int, optional
#对角线的位置，大于零位于对角线上面，小于零则在下面。


import numpy as np
arr=np.diag(v=1+np.arange(4),k=-1)
print(arr)