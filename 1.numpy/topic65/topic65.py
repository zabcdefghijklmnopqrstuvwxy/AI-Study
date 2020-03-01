#权重weights，以及最小bin的数量minlength。
#若不指定权重，则默认x每个位置上的权重相等且为1。若给定不同位置的权重，则返回加权和。

#若不规定最小bin的个数，则默认的个数为（x的最大值+1）。比如最大值是2，则bin的个数为3，即[0 1 2]。

#若规定bin的个数（需大于默认值否则无效），则bin的个数等于设定值。比如np.bincount(np.array([3,1,9]), minlength=8)，若不指定minlength，输出的个数应该为9+1=10个。但此时指定的minlength小于10，小于默认状态下的数量，参数不再作用。返回的长度仍为10。如果np.bincount(np.array([3,1,9]), minlength=20)，指定的minlength大于10，那么返回的长度就是20。

#np.bincount()总结
#返回值中的每个bin，给出了它的索引值在x中出现的次数（在默认权重下）。
#返回值中的每个bin，给出了它的索引值，由于在x中出现在不同位置所导致权重不同，而计算的加权和。
#其中，索引的长度可由minlength规定。


import numpy as np 

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]

F = np.bincount(I,weights=X)
print(F)