import numpy as np 

Z=np.dtype([('pos',[('x',int),('y',int)]),('color',[('r',int),('g',int),('b',int)])])
E=np.array([((5,3),(100,100,100))],dtype=Z)

print(E)