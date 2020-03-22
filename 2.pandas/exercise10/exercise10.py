#练习十：删除数据
#1. 导入必要的库
import pandas as pd 
import numpy as np 

#2.从以下地址导入数据iris.csv
path="iris.csv"

#3.将数据框命名为iris
iris=pd.read_csv(path)

#4.创建数据框的列名称为'sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'
iris=pd.read_csv(path,names=['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])

#5.数据框中有缺失值吗？
null=iris.isnull().sum()

#6.将列petal_length的第10到19行设置为缺失值
iris.loc[10:19,'petal_length']=np.nan

#7.将缺失值全部替换为1.0W
iris=iris.fillna('1.0')

#8.删除列class
del iris['class']

#9.将数据框前三行设置为缺失值
iris.loc[:3,:]=np.nan

#10.删除有缺失值的行
iris.dropna(how='any')

#11.重新设置索引
iris.reset_index(drop=True)



