#numpy.random.random(size=None)
#产生[0.0, 1.0)之间的浮点数

#numpy.random.randint(low, high=None, size=None, dtype='I')
#生成size个整数，取值区间为[low, high)，若没有输入参数high则取值区间为[0, low)

import numpy as np

arr=np.random.randint(0,99,(3,3,3))
print(arr)
