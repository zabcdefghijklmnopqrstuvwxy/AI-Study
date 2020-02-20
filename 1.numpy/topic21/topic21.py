#numpy中的tile()函数
#描述
#Numpy 的 tile() 用于叠加（复制）指定的数据结构。

#语法
#tile()方法语法：

#tile(dataStructure, (shape);
#参数
#dataStructure
# -- 被叠加的数据结构
#shape  --以什么shape叠加
#返回值
#返回叠加得到的数据结构，一般是ndarray。

import numpy as np
pat=[[1,0],[0,1]]
arr=np.tile(pat,(4,4))
print(arr)
