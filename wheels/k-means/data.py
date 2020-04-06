import numpy as np 
import pandas as pd 
from scipy.io import loadmat
import matplotlib.pyplot as plt 

mat=loadmat('ex7data2.mat')

def findClosestCentroids(Datas, centroids):  # Datas:array, centroids:array
    clustering = []  # 储存聚类结果
    # 遍历每个样本点
    for i in range(len(Datas)):
        data = Datas[i]
        diff = data - centroids   # 数据类型都为np.array
        dist = 0
        for j in range(len(diff[0])):
            dist += diff[:,j]**2   # 求欧式距离       
        min_index = np.argmin(dist)  # 找出距离最小的下标
        clustering.append(min_index)
    return np.array(clustering)

def computMeans(Datas, clustering):
    centroids = []
    for i in range(len(np.unique(clustering))):  # np.unique计算聚类个数
        u_k = np.mean(Datas[clustering==i], axis=0)  # 求每列的平均值
        centroids.append(u_k)
    return np.array(centroids)

def plotdata(data, centroids, clusted=None):   # data:数据， centroids:迭代后所有中心点， clusted:最后一次聚类结果
    colors = ['b','g','gold','darkorange','salmon','olivedrab', 
              'maroon', 'navy', 'sienna', 'tomato', 'lightgray', 'gainsboro'
             'coral', 'aliceblue', 'dimgray', 'mintcream', 'mintcream']  # 定义颜色，用不同颜色表示聚类结果
    
    assert len(centroids[0]) <= len(colors), 'colors are not enough '  # 检查颜色和中心点维度
    
    clust_data = []  # 存储聚好类的数据,同一个类放在同一个列表中
    if clusted is not None: 
        for i in range(centroids[0].shape[0]):
            x_i = data[clusted==i]
            clust_data.append(x_i)  # x_i is np.array
    else:
        clust_data = [data]  # 未进行聚类，默认将其作为一个类
     
    # 用不同颜色绘制数据点
    plt.figure(figsize=(8,5)) 
    for i in range(len(clust_data)):
        plt.scatter(clust_data[i][:, 0], clust_data[i][:, 1], color=colors[i], label='cluster %d'%(i+1))
        
    plt.legend()
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    
    # 绘制中心点
    centroid_x = [] 
    centroid_y = []
    for centroid in centroids:
        centroid_x.append(centroid[:,0])
        centroid_y.append(centroid[:,1])
    plt.plot(centroid_x, centroid_y, 'r*--', markersize=14)
    plt.show()

def run_k_means(Datas, centroids, iters):
    all_centroids = [centroids]
    for i in range(iters):
        clusted = findClosestCentroids(Datas, centroids)
        centroids = computMeans(Datas, clusted)
        all_centroids.append(centroids)
    return clusted, all_centroids

X = mat['X']  # get data

centroids = np.array([[3,3], [6,2], [8,5]])   #随机定义三个聚类中心点
clusted, all_centroids = run_k_means(X, centroids, 30)  #迭代30次反复规划聚类中心点
plotdata(X, all_centroids, clusted)


