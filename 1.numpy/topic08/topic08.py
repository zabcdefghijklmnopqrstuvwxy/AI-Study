#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#参数说明：

#名称	描述
#object	数组或嵌套的数列
#dtype	数组元素的数据类型，可选
#copy	对象是否需要复制，可选
#order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
#subok	默认返回一个与基类类型一致的数组
#ndmin	指定生成数组的最小维度

#a[i:j:s]表示：i,j与上面的一样，但s表示步进，缺省为1.
#所以a[i:j:1]相当于a[i:j]
#当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
#所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
arr = arr[::-1]
print(arr)