#柯西矩阵描述如下：
#[1/(x1+y1)  1/(x1+y2) ...... 1/(x1+yn)]
#[1/(x2+y1)  1/(x2+y2) .......1/(x2+yn)]
#[......................................]
#[1/(xm-1 + y1) 1/(xm-1+y2)..1/(xm-1+yn)]
#[1/(xm+y1)  1/(xm+y2)........1/(xm+yn)]
#柯西矩阵特点：
#第一，任意一个子阵都是奇异矩阵，存在逆矩阵
#第二，柯西矩阵在伽罗华域的求逆运算，可以在O(n^2)的运算复杂度内完成

#numpy.add() :数组相加
#numpy.subtract():数组相减
#numpy.multiply():数组相乘
#numpy.devide():数组相除

#np.subtract.outer(b,a)是b[:,None]-a的函数对应
#其含义是：

#有两个向量a、b，要实现a中的每个元素与b中的每个元素进行比较

#numpy.linalg模块包含线性代数的函数。使用这个模块，可以计算逆矩阵、求特征值、解线性方程组以及求解行列式等。
#计算逆矩阵 linalg.inv(A) 注：矩阵必须是方阵且可逆，否则会抛出LinAlgError异常。
#计算行列式 linalg.det(A)
#linalg模块中，eigvals()函数可以计算矩阵的特征值，而eig()函数可以返回一个包含特征值和对应的特征向量的元组
#linalg中的函数solve()可以求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维或二维的数组，x 是未知变量
#SVD（Singular Value Decomposition，奇异值分解）是一种因子分解运算，将一个矩阵分解为3个矩阵的乘积;
#linalg模块中的svd()函数可以对矩阵进行奇异值分解,该函数返回3个矩阵——U、Sigma和V，其中U和V是正交矩阵，
#Sigma包含输入矩阵的奇异值。
#linalg模块中的 pinv()函数可进行求解广义逆矩阵；
#注：inv函数只接受方阵作为输入矩阵，而pinv函数则没有这个限制

import numpy as np 

X = np.arange(8)
Y = X + 0.5
#C = 1.0 / np.subtract.outer(X, Y)
C = 1.0 / np.add.outer(X, Y)
print(C)
print(np.linalg.det(C))
