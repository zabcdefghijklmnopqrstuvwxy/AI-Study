#NumPy 迭代数组
#NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
#迭代器最基本的任务的可以完成对数组元素的访问。

#不是使用标准 C 或者 Fortran 顺序，选择的顺序是和数组内存布局一致的，这样做是为了提升访问的效率，默认是行序优先（row-major order，或者说是 C-order）。
#这反映了默认情况下只需访问每个元素，而无需考虑其特定顺序。我们可以通过迭代上述数组的转置来看到这一点，并与以 C 顺序访问数组转置的 copy 方式做对比

#nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），为了在遍历数组的同时，
#实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。

#切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同

import numpy as np 
A = np.arange(3).reshape(3,1)
B = np.arange(3).reshape(1,3)
print(f"(3,1) arr is \n{A}\n")
print(f"(1,3) arr is \n{B}\n")

it = np.nditer([A,B,None])
for x,y,z in it: 
    z[...] = x + y
print(it.operands[2])


