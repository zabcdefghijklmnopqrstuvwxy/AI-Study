#函数原型：  numpy.random.uniform(low,high,size)

#功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.

#参数介绍: 
    
#    low: 采样下界，float类型，默认值为0；
#    high: 采样上界，float类型，默认值为1；
#    size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出m*n*k个样本，缺省时输出1个值。

#返回值：ndarray类型，其形状和参数size中描述一致。

#这里顺便说下ndarray类型，表示一个N维数组对象，其有一个shape（表维度大小）和dtype（说明数组数据类型的对象），使用zeros和ones函数可以创建数据全0或全1的数组，原型：
#numpy.ones(shape,dtype=None,order='C'),
#其中，shape表数组形状（m*n）,dtype表类型,order表是以C还是fortran形式存放数据。

#2. 类似uniform,还有以下随机数产生函数：

 #   a. randint: 原型：numpy.random.randint(low, high=None, size=None, dtype='l')，产生随机整数；
 #   b. random_integers: 原型： numpy.random.random_integers(low, high=None, size=None)，在闭区间上产生随机整数；
 #   c. random_sample: 原型： numpy.random.random_sample(size=None)，在[0.0,1.0)上随机采样；
 #   d. random: 原型： numpy.random.random(size=None)，和random_sample一样，是random_sample的别名；
 #   e. rand: 原型： numpy.random.rand(d0, d1, ..., dn)，产生d0 - d1 - ... - dn形状的在[0,1)上均匀分布的float型数。
 #   f. randn: 原型：numpy.random.randn（d0,d1,...,dn),产生d0 - d1 - ... - dn形状的标准正态分布的float型数。

#sum() 没有axis参数表示全部数据相加
#axis=0，表示按列相加
#axis=1，表示按行相加


import numpy as np
arr = np.random.uniform(0,100,size=(5,5))
sum=arr.sum()
arr=arr/sum
print(arr)
