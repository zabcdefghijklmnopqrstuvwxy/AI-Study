#numpy.floor 向下取整
#numpy.floor 返回不大于输入参数的最大整数。 即对于输入值 x ，将返回最大的整数 i ，使得 i <= x。 
#注意在Python中，向下取整总是从 0 舍入。
#numpy.ceil 向上取整
#numpy.ceil 函数返回输入值的上限，即对于输入 x ，返回最小的整数 i ，使得 i> = x。

#numpy.trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'trunc'>
#以元素方式返回输入的截断值。
#标量x的截断值是最接近的整数i，它比x更接近零。简而言之，丢弃带符号数x的小数部分。

#参数：
#x ：array_like 输入数据。 out ：ndarray，None或ndarray和None的元组，
#可选 存储结果的位置。如果提供，它必须具有输入的形状。

#如果未提供或None，则返回新分配的数组。
#元组（仅可作为关键字参数）的长度必须等于输出的数量。 
#其中 ： array_like，可选 值True表示计算该位置的ufunc，
#值False表示仅将值保留在输出中。 
#** kwargs 对于其他仅关键字参数，请参阅 ufunc文档。

#返回：
#y ：ndarray或标量x中每个元素的截断值。如果x是标量，则这是标量。

import numpy as np 
Z = np.random.uniform(0,10,10)

print(f"float num is {Z}")
print(f"Z//1={Z//1}")
print (f"Z-Z%1={Z - Z%1}")
print (f"np.floor(Z)={np.floor(Z)}")
print (f"np.ceil(Z)-1={np.ceil(Z)-1}")
print (f"Z.astype(int)={Z.astype(int)}")
print (f"np.trunc(Z)={np.trunc(Z)}")