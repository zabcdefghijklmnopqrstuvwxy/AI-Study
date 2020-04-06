import numpy as np 
from skimage import io 
import pandas as pd 
import matplotlib.pyplot as plt 

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

def run_k_means(Datas, centroids, iters):
    all_centroids = [centroids]
    for i in range(iters):
        clusted = findClosestCentroids(Datas, centroids)
        centroids = computMeans(Datas, clusted)
        all_centroids.append(centroids)
    return clusted, all_centroids

sample_image=io.imread("bird_small.png")

sample_image = sample_image/255   # 将数据归一化到0-1

data = sample_image.reshape(-1, 3)  # 将图片像素大小重置，每一个像素点代表一个样本

k = 16  #  聚类个数

centroids = np.random.random(size=(k,3))

clusted, all_centroids = run_k_means(data, centroids, 30)

img = np.zeros(data.shape)  # 初始化图片
last_centroids = all_centroids[-1]  # 最后一聚类质心

for i in range(len(last_centroids)):  # 利用聚类质心替换图片中元素
    img[clusted==i] = last_centroids[i]

img = img.reshape(128, 128, 3)  # 转换大小

fig, axs = plt.subplots(1, 2, figsize=(10,6))
axs[0].imshow(sample_image)
axs[1].imshow(img)
plt.show()