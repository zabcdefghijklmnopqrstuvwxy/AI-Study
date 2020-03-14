#1.导入pandas
import pandas as pd 
import numpy as np 
#2.导入数据集
#3.数据集存入csv数据框中
path = "chipotle.tsv"
csv = pd.read_csv(path,sep='\t')
#4.查看前十行内容
pd.set_option('display.max_rows', 100)
csv.head(10)   #显示前十行信息
#5.数据集有多少列
csv.shape[0]   #显示总共的行数
#6.打印出全部的列名称
csv.columns    #显示列项目
#7.数据的索引
csv.index      #显示行项目
#8.被下单数最多商品是什么
maxitem=csv[['quantity','item_name']].groupby('item_name').sum().sort_values(by='quantity',ascending=False).head(1)

#9.在item_name这一列中，一共有多少商品被下单
cnt=pd.unique(csv['item_name']).size

#10.在choice_description中，下单次数最多的商品是什么?
choice = csv['choice_description'].value_counts().head(1)

#11.一共有多少商品被下单
total=csv['quantity'].sum()

#12.将item_price转换为浮点数
change=lambda x:float(x[1:-1])
csv['value']=csv['item_price'].apply(change)

#13.在该数据集对应的时期内，收入(revenue)是多少?
csv['revenue'] = csv['quantity']*csv['item_price']
reve=csv['revenue'].sum()

#14.在该数据集对应的时期内，一共有多少订单
csv['quantity'].sum()

#15.每一单(order)对应的平均总价是多少?
arr=csv.groupby('order_id').sum()
ave=arr['value']/arr['quantity']
print(ave)

#16.一共有多少种不同的商品被售出?
num=csv['item_name'].nunique()
