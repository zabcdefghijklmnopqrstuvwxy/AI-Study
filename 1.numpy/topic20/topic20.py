#numpy.unravel_index()函数的作用是获取一个/组int类型的索引值在一个多维数组中的位置
#numpy.unravel_index(indices, dims, order='C')

#参数说明：indices数组
#dims数组的维度大小
#order:{C,F}（C行为主，F列为主）
#返回:unraveled_coords为n维数组的元组

import numpy as np
index=np.unravel_index(100,(6,7,8))
print(index)