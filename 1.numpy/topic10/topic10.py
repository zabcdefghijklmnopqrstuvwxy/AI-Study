#列表解析功能是在Python2.0加入的，列表解析允许在for循环语句中使用表达式对列表成员进行迭代操作。列表解析的语法如下:

#[expr for iter_var in list if cond_expr]

#列表解析语法的核心是for循环语句，其中expr是条件表达式，该表达式用于list的每个成员，最后的结果值是该表达式产生的列表，
#iter_var是迭代变量，指向list的成员，cond_expr是条件表达式，该条件表达式会过滤或捕获满足条件的list成员，
#cond_expr不是必须的。


import numpy as np

arr=np.array([1,2,0,0,4,0])

index = [i for i in range(len(arr)) if arr[i] == 0]
print(index)

