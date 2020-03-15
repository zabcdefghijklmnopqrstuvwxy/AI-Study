#练习二：数据过滤与排序

#1.导入Pandas
import pandas as pd 
import numpy as np 

#2.从如下地址导入数据集Euro2012_stats.csv
path="Euro2012_stats.csv"

#3.将数据集存入一个名为euro12的数据框内
euro12=pd.read_csv(path)

#4.只选取Goals这一列
Goals=euro12['Goals']

#5.有多少球队参与了2012欧洲杯？
TeamNum=euro12['Team'].nunique()

#6.该数据集中一共有多少列?
colnum=euro12.shape[1]

#7.将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline=euro12[['Team','Yellow Cards','Red Cards']]

#8.对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline.sort_values(['Red Cards','Yellow Cards'],ascending=[False,False])

#9.计算每个球队（意思是所有球队的黄牌平均值）拿到的黄牌数的平均值（不要小数）
yellowmean=int(euro12['Yellow Cards'].sum()/TeamNum)

#10.找到进球数Goals超过6的球队数据
arr=euro12[euro12['Goals']>6]

#11.选取以字母G开头的球队数据
euro12[euro12['Team'].str.startswith('G')]

#12.选取前7列
seven=euro12.iloc[:,0:7]

#13.选取除了最后3列之外的全部列
last3=euro12.iloc[:,0:-3]

#14.找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
shoot=euro12.loc[euro12['Team'].isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]
print(shoot)
