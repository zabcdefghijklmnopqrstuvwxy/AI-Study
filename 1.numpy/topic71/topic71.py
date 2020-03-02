import numpy as np 

A=np.random.randint(0,10,(5,5,3))
B=np.random.randint(0,10,(5,5))

print(A*B[:,:,None])