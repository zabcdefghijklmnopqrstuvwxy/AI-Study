#unique(x)	        计算x中唯一元素，并返回有序的结果	        np.unique(s0)	[1 2 3 4 5]
#intersect1d(x,y)	交集，并返回有序结果	                   np.intersect1d(s1,s2)	[ 0 6 12 18 24]
#union1d(x,y)	    并集，并返回有序结果	                   np.union1d(s1,s2)	[ 0 2 3 4 6 8 9 10 12 14 15 16 18 20 21 22 24 26 27 28]
#setdiff1d(x,y)	    集合差，即元素在x中且不再y中	            np.setdiff1d(s1,s2)	[ 2 4 8 10 14 16 20 22 26 28]
#setxor1d(x,y)	    集合对称差，只存在x和y中的元素集合	        np.setxor1d(s1,s2)	[ 2 3 4 8 9 10 14 15 16 20 21 22 26 27 28]
#in1d(x,y)	        得到一个”x的元素是否包含于y”的布尔行数组	np.in1d(s2,s1)	[ True False True False True False True False True False]

import numpy as np 
arr1=np.random.randint(1,10,(1,10))
arr2=np.random.randint(1,10,(1,10))
print(f"arr1 is {arr1}")
print(f"arr2 is {arr2}")
arr3=np.intersect1d(arr1,arr2)
print(f"arr1 and arr2 common is {arr3}")

