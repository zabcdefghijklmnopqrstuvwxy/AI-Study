#Numpy中也有逻辑判断的函数，即logical_and()，logical_or(), logical_not(), logical_xor() 这几个函数的大致用法相同，功能上有较大的区别，下面一一详解

#2. numpy. logical_and()
#2.1 语法
#numpy.logical_and(x1, x2) 
#返回X1和X2与逻辑后的布尔值。

#2.2 主要参数：
#x1，x2：array_like
#输入数组。 x1和x2必须具有相同的形状。
#随着版本的变化，函数的参数也在更新，更多详情点击 查看。
#返回：
#y：ndarray或bool
#布尔结果，与x1和x2的相应元素上的逻辑AND运算，结果和x1和x2形状相同。 如果x1和x2都是标量，则也返回标量。

#numpy.logical_or(x1, x2) 
#返回X1和X2或逻辑后的布尔值。

#3.2 主要参数：
#x1，x2：array_like
#输入数组。 x1和x2必须具有相同的形状。
#随着版本的变化，函数的参数也在更新，更多详情点击 查看。
#返回：
#y：ndarray或bool
#布尔结果，与x1和x2的相应元素上的逻辑OR运算，结果和x1和x2形状相同。 如果x1和x2都是标量，则也返回标量。

#numpy.logical_not(x) 
#返回X非逻辑后的布尔值。

#4.2 主要参数：
#x：array_like
#输入数组。
#随着版本的变化，函数的参数也在更新，更多详情点击 查看。
#返回：
#y：ndarray或bool
#布尔结果，与x的相应元素上的逻辑NOT运算，结果和x形状相同。 如果x是标量，则也返回标量。

import numpy as np 
Z = np.random.randint(0,2,100)

print(f"int arr is \n{Z}\n")
np.logical_not(Z, out=Z)
print(f"logical not int arr is \n{Z}\n")


Z = np.random.uniform(-1.0,1.0,10)
print(f"float arr is \n{Z}\n")
np.negative(Z, out=Z)
print(f"negative float arr is \n{Z}\n")
