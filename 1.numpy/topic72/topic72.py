import numpy as np 

arr=np.arange(25,dtype=int).reshape(5,5)

arr[[0,1],] = arr[[1,0],]
print(arr)