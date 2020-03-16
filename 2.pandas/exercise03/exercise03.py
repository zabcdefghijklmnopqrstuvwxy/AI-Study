#练习三：数据分组
#1.导入Pandas
import pandas as pd 

#2.从如下地址导入数据集drink.csv
path="drinks.csv"

#3.将数据集存入一个名为drinks的数据框内
drinks=pd.read_csv(path)

#4.哪个大陆(continent)平均消耗的啤酒(beer)最多?
drinks[['continent','beer_servings']].groupby(by='continent').mean().sort_values('beer_servings',ascending=False).head(1)

#5.打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
drinks[['continent','wine_servings']].groupby(by='continent').describe()

#6.打印出每个大陆每种酒类别的消耗平均值
beermean=drinks.groupby('continent').mean()

#7.打印出每个大陆每种酒类别的消耗中位数median()
beermedian=drinks.groupby('continent').median()

#8.打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
spirit=drinks[['spirit_servings','continent']].groupby('continent').agg(['mean','max','min'])

