#练习九：时间序列
#1. 导入必要的库
import pandas as pd 
import matplotlib.pyplot as plt

#2.从以下地址导入数据Apple_stock.csv
path="Apple_stock.csv"

#3.将数据框命名为apple
apple=pd.read_csv(path)

#4.查看每一列的数据类型
apple.dtypes

#5.将Date这个列转换为datetime类型
apple.Date=pd.to_datetime(apple['Date'])

#6.将Date设置为索引
apple=apple.set_index('Date')

#7.有重复的日期吗？
apple.index.is_unique

#8.将index设置为升序
apple.sort_index()

#9.找到每个月的最后一个交易日(business day)
bd=apple.resample('BM').sum()

#10.数据集中最早的日期和最晚的日期相差多少天？
day=(apple.index.max()-apple.index.min()).days

#11.在数据中一共有多少个月？
month=apple.resample('M').count()
len(month.index)

#12.按照时间顺序可视化Adj Close值
apple['Adj Close'].plot(title = 'Apple Stock').get_figure().set_size_inches(9,5)
plt.show()

