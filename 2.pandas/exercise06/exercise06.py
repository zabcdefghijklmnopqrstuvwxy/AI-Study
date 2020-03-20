#练习六：统计
#1.导入必要的库
import pandas as pd 
import datetime

#2.从以下地址导入数据wind.data
path="wind.data"
wind=pd.read_csv(path,sep="\\s+")

#3.将数据做存储并且设置前三列为合适的索引
wind=pd.read_csv(path,sep="\\s+",parse_dates=[[0,1,2]])

#4.1961年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
def fix_year(x):
    year=x.year-100 if x.year>1979 else x.year
    return datetime.date(year,x.month,x.day)

wind['Yr_Mo_Dy']=wind['Yr_Mo_Dy'].apply(fix_year)

#5.将日期设为索引，注意数据类型，应该是datetime64[ns]
wind['Yr_Mo_Dy']=pd.to_datetime(wind['Yr_Mo_Dy'])
wind=wind.set_index('Yr_Mo_Dy')

#6.对应每一个location，一共有多少数据值缺失
wind.isnull().sum()

#7.对应每一个location，一共有多少完整的数据值
wind.notnull().sum()
# count也可以计算非空数值
# print(wind.count())

#8.对于全体数据，计算风速的平均值
wind.mean().mean()

#9.创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
loc_stats=pd.DataFrame()
loc_stats=wind.agg(['min','max','mean','std'])

#10.创建一个名为day_stats的数据框去计算并存储所有location的每天的风速最小值，最大值，平均值和标准差
day_stats=pd.DataFrame()
for i in range(wind.shape[0]):
    day_stats[i]=wind.iloc[i].agg(['min','max','mean','std'])

#11.对于每一个location，计算一月份的平均风速
wind[wind.index.month==1].mean()

#12.对于数据记录按照年为频率取样（没说清楚，答案写的是取出每年一月一号的数据）
wind.resample('MS').mean()

#13.对于数据记录按照月为频率取样
wind.resample('M').mean()

