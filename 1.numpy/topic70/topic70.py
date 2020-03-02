import numpy as np 
arr=np.arange(1,6)
nz = 3
Z = np.zeros(len(arr) + (len(arr)-1)*(nz))
Z[::nz+1] = arr
print(Z)
