#numpy中的mean() 函数定义： 
#numpy.mean(a, axis, dtype, out，keepdims )

#mean()函数功能：求取均值 
#经常操作的参数为axis，以m * n矩阵举例：

#axis 不设置值，对 m*n 个数求均值，返回一个实数
#axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
#axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵

import numpy as np

arr=np.random.randint(1,99,30)
avr=arr.mean()
print(arr)
print(avr)
