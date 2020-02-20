#Nan：Not a number
#Inf：Infinity(无穷大）
#当然容易搞混的还有None，None是python中用于标识空缺数据，Nan是nunpy和pandas中用于标识空缺数据，
#None是一个python特殊的数据类型， 但是NaN却是用一个特殊的float，此处我仅针对Nan和Inf的处理。

import numpy as np

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)