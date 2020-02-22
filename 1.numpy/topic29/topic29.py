#描述
#round() 方法返回浮点数x的四舍五入值。

#语法
#以下是 round() 方法的语法:

#round( x [, n]  )
#参数
#x -- 数值表达式。
#n -- 数值表达式。
#返回值
#返回浮点数x的四舍五入值。

import numpy as np 
arr=np.random.uniform(1,10,size=(1,10))
print(arr)
arr=np.round(arr,0)
print(arr)