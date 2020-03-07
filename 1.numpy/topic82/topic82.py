#函数：np.linalg.svd(a,full_matrices=1,compute_uv=1)。

#参数：
#a是一个形如(M,N)矩阵
#full_matrices的取值是为0或者1，默认值为1，这时u的大小为(M,M)，v的大小为(N,N) 。否则u的大小为(M,K)，v的大小为(K,N) ，K=min(M,N)。
#compute_uv的取值是为0或者1，默认值为1，表示计算u,s,v。为0的时候只计算s。

#返回值：
#总共有三个返回值u,s,v
#u大小为(M,M)，s大小为(M,N)，v大小为(N,N)。
#A = u*s*v
#其中s是对矩阵a的奇异值分解。s除了对角元素不为0，其他元素都为0，并且对角元素从大到小排列。s中有n个奇异值，一般排在后面的比较接近0，所以仅保留比较大的r个奇异值。 

#在线性代数中，一个矩阵A的列秩是A的线性独立的纵列的极大数，通常表示为r(A)，rk(A)或rank A。 


import numpy as np 

Z = np.random.uniform(0,1,(10,10))
U, S, V = np.linalg.svd(Z) 
rank = np.sum(S > 1e-10)
print(rank)

