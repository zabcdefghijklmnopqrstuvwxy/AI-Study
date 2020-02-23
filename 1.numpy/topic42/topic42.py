#比较两个向量是否相同直接==就行，但是相近的话就不一样了，当然可以自己实现，这里numpy提供了方法，
#numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
#a,b两个向量
#rtol : float
#The relative tolerance parameter
#atol : float
#The absolute tolerance parameter
#equal_nan : bool
#是否匹配空nan值
#return 是否相近

#array_equal(a1,a2)
#Parameters:	参数
#a1, a2 : array_like
#Input arrays.
#Returns:	返回值
#b : bool
#Returns True if the arrays are equal.

import numpy as np 
A=np.random.randint(0,10,size=(1,10))
B=np.random.randint(0,10,size=(1,10))
print(f"A is {A}")
print(f"B is {B}")

res=np.array_equal(A,B)

if res:
    print("A and B is equal")
else:
    print("A and B is not equal")
