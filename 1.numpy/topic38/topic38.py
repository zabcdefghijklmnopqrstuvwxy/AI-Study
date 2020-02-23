#1.生成器
#在 Python 中，一边循环一边计算的机制，称为生成器（Generator）；
#生成器是一个返回迭代器的函数，只能用于迭代操作；
#2.什么是生成器函数#
#生成器是Python中的一个对象，对这个对象进行操作，可以依次生产出按生成器内部运算产生的数据；
#生成器函数指的是函数体中包含yield关键字的函数（yield就是专门给生成器用的return）；
#生成器可以通过生成器表达式和生成器函数获取到；
#3.生成器函数的定义
#def add():
#    for i in range(10):
#        yield i
#g = add()
#print(g)  # <generator object add at 0x10f6110f8>
#print(next(g))  # 0
#print(next(g))  # 1
#我们可以通过yield关键字来定义一个生成器函数，这个生成器函数返回值就是一个生成器对象；
#4.生成器函数的调用
#def gen():
#    print('111111')
#    yield '111111'
#    print('222222')
#    yield '222222'
#    print('333333')
#    yield '333333'
#g = gen()
#print(g)  # <generator object gen at 0x0026BBF0>
#next(g)   # 111111
#next(g)   # 222222
#next(g)   # 333333
#next(g, 'over')
 
#生成器函数可以使用next()迭代，且每次next()只会返回一次yield的值，然后暂停，下次一次next()时会在当前位置继续，如果没有元素可以迭代了，还 执在行next()则需要给定一个默认值，不给默认值会报错；
#如果在生成器函数中使用return，则会终止迭代，且不能得到返回值；

#numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。

#numpy.fromiter(iterable, dtype, count=-1)
#参数	描述
#iterable	可迭代对象
#dtype	返回数组的数据类型
#count	读取的数据数量，默认为-1，读取所有数据

import numpy as np

def gener():
    for x in range(10):
        yield x

Z=np.fromiter(gener(),dtype=float,count=-1)
print(Z)
