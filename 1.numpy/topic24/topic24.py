#首先先给一个比较简单的用法解释：
#*：             根据数据类型的不同，可能是做点乘运算，也可能做矩阵乘法运算
#@：             只做矩阵乘法运算
#.dot：          只做矩阵乘法运算
#np.mutiply：只做点乘运算

import numpy as np 
Z = np.ones((5,3),dtype=int) @ np.ones((3,2),dtype=int)
print(Z)