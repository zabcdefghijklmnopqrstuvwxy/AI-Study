#python主要的算术运算符与C/C++类似。+, -, *, /, //, **, ~, %分别
#表示加法或者取正、减法或者取负、乘法、除法、整除、乘方、取补、取余。

import numpy as np 

print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
