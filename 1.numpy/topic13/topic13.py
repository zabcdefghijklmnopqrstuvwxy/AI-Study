#numpy中的max()和min()函数
#1）如果直接用min(),那么返回的是整个矩阵中元素的最小值

#2）如果用min(0)或者min(axis=0)),那么返回的是所有列中每一列的最小值，返回一个1*n的数组

#3）如果用min(1)或者min(axis=1)),那么返回的是所有行中每一行的最小值，返回一个1*n的数组

#对于max()函数，同上。

import numpy as np

arr=np.random.randint(0,99,(10,10))
max = arr.max()
min = arr.min()
print(arr)
print("10x10中的最大数值是%d"%(max))
print("10x10中的最小数值是%d"%(min))

