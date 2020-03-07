import numpy as np 
N=10
arr=np.random.randint(0,N,20)
print(arr)
Z=np.arange(N)
print(Z[(np.bincount(arr)).argmax()])
