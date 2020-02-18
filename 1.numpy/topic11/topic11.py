#numpy.eye（N，M =无，k = 0，dtype = <class’flove’>，order =‘C’ ）
#返回一个二维数组，其中对角线为1，零点为零。

#参数：	
#N ： int
#输出中的行数。
#M ： int，可选
#输出中的列数。如果无，默认为Ñ。
#k ： int，可选
#对角线的索引：0（默认值）指的是主对角线，正值指的是上对角线，负值指的是下对角线。
#dtype ： 数据类型，可选
#返回数组的数据类型。
#order： {‘C’，‘F’}，可选
#输出是否应以内存中的行主（C风格）或列主（Fortran风格）顺序存储。

#3*3单位矩阵即
# 1 0 0
# 0 1 0
# 0 0 1

import numpy as np

arr=np.eye(3,dtype=int)
print(arr)

