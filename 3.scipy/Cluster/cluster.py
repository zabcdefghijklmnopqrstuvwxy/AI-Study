from scipy.cluster.vq import kmeans,vq,whiten
from numpy.random import rand 
from numpy import vstack,array

data=vstack((rand(10,3) + array([.5,.5,.5]),rand(100,3)))

data = whiten(data)             # 美白数据

centroids,_ = kmeans(data,3)    # 从数据中查找到三个簇，并返回三个簇的质心

print(centroids)

clx,_ = vq(data,centroids)      #导出三个簇的数据

print(clx)