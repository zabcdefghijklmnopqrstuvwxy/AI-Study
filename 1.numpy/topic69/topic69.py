#numpy.diag(v,k=0) 官方文档
#以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转换成方阵（非对角线元素为0）.两种功能角色转变取决于输入的v。1

#更深层的见numpy.diagnal()

#参数详解：

#v : array_like.
#如果v是2D数组，返回k位置的对角线。

#如果v是1D数组，返回一个v作为k位置对角线的2维数组。

#k : int, optional
#对角线的位置，大于零位于对角线上面，小于零则在下面。

#np.einsum 的第一个参数是一个string，由两个substring组成，由逗号分隔。第二个和第三个参数都是np.array
#这个函数的功能呢，就是让我们定义A 和B 两个数组的运算。
#那么什么是定义运算呢？基本上我们可以理解为定义下面一句话（设A 和B运算的结果是C），C的某一个元素是由A的某一些元素与B的某一些元素通过什么操作得到的。
#那要定义运算，首先我们要有办法指出每个元素在A 或B 中的位置（需要indices）。（然后才能定义运算：例如，让A的某个位置的元素和B的某个位置的元素相乘/相加等等）
#注意，这边的元素要求是scalar！（例如，3d-array需要3个维度对应到一个实数项（scalar），而2个维度对应的是vector，而1个维度对应的是matrix）
#那第一参数我们就在做上面这件事，, 分割的两个substring定义了所需要的维度指代（先只看->的左边）每一个字母对应相应的维度（或者axis，从小到大）），例如上面的代码中，第一个substringijk 对应到第一个数组A 的indices，那么定义运算的时候指A 的scalar就是: A[i,j,k] 表示 ，同理我们定义运算的时候指B的scalar就是B[k,m] 的indices

#没有->
#此时的运算规则很简单，就是将两个substring重合的indices去做和（这样就去掉了这个维度），其余的保留作为index
#有->
#有-> 和上面略有不同。-> 右边定义了结果的样子（因此也定义了运算）

import numpy as np  

A=np.random.randint(0,10,size=(5,5))
B=np.random.randint(0,10,size=(5,5))

X=np.diag(np.dot(A,B))
Y=np.sum(A * B.T, axis=1) 
Z=np.einsum("ij,ji->i", A, B)  

print(f"slow diag is {X}")
print(f"fast diag is {Y}")
print(f"faster diag is {Z}")

