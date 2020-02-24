import numpy as np 
arr=np.zeros(shape=(5,5),dtype=[('x',float),('y',float)])
arr['x'],arr['y']=np.linspace(0,1,5),np.linspace(0,1,5)
print(arr)