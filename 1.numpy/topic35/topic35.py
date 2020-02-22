import numpy as np 
#A=np.random.randint(1,9,size=(3,3))
#B=np.random.randint(1,9,size=(3,3))
#print(A)
#print(B)
#C=(A+B)/(-A/2)
#print(C)

A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)
print(A)