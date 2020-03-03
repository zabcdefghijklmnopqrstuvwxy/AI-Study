#repeat函数的作用：①扩充数组元素 ②降低数组维度
#numpy.repeat(a, repeats, axis=None)：若axis=None，对于多维数组而言，可以将多维数组变化为一维数组，然后再根据repeats参数扩充数组元素；若axis=M，表示数组在轴M上扩充数组元素。

#repeats为整数N，axis=None：数组arr首先被扁平化，然后将数组arr中的各个元素依次重复N次
#repeats为整数数组rp_arr，axis=None：数组arr首先被扁平化，然后再将数组arr中元素依次重复对应rp_arr数组中元素对应次数。若rp_arr为一个值的一维数组，则数组arr中各个元素重复相同次数，
#否则rp_arr数组长度必须和数组arr的长度相等，否则报错

import numpy as np 

arr=np.array([1,1,3,4,5])
C=np.bincount(arr)

A=np.repeat(np.arange(len(C)),C)

print(f"arr is \n{arr}\n")
print(f"A is \n{A}\n")