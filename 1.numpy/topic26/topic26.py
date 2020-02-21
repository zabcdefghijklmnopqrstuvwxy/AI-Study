#python自带的sum函数签名如下：
#sum(iterable,[start])
#后一个参数指定的是初始化值，会加到结果中去。故结果是-1+1+2+3+4=9。
#numpy中sum函数签名为：
#numpy.sum(a,axis=None,dtype=None,out=None,keepdims=,initial=)
#不使用命名参数，-1传给了axis，结果为10。如果要指定初始值，这样用sum(range(1,5),initial=-1)。

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))