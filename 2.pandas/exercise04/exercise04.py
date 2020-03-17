#练习四：Apply函数
#1.导入Pandas,numpy
import numpy as np 
import pandas as pd 

#2. 从如下地址导入数据集US_Crime_Rates_1960_2014.csv
path="US_Crime_Rates_1960_2014.csv"

#3. 将数据集存入一个名为crime的数据框内
crime=pd.read_csv(path)

#4. 每一列(column)的数据类型是什么样的？
crime.dtypes

#5.将Year的数据类型转换为 datetime64
crime.Year=pd.to_datetime(crime.Year,format='%Y')

#6.将列Year设置为数据框的索引
crime.Year=crime.set_index('Year',drop=True)

#7.删除名为Total的列
del crime['Total']

#8.按照每十年Year对数据框进行分组并求和
#crimes=crime.resample('10Y').sum()

#9.何时是美国历史上生存最危险的年代？
print(crime.idxmax(0))