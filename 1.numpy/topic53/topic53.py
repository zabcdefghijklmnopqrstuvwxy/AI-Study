#astype：转换数组的数据类型。

#int32 --> float64        完全ojbk
#float64 --> int32        会将小数部分截断
#string_ --> float64      如果字符串数组表示的全是数字，也可以用astype转化为数值类型

import numpy as np 
arr=np.arange(10,dtype=np.float)
print(f"float array {arr}")
Z=arr.astype(np.int)
print(f"int array {Z}")