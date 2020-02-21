
#dtype 对象是使用以下语法构造的：

#numpy.dtype(object, align, copy)
#object - 要转换为的数据类型对象
#align - 如果为 true，填充字段使其类似 C 的结构体。
#copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用

import numpy as np
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])

print(color)