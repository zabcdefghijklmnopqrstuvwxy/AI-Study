#练习七：可视化
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#1.将数据框命令为titanic
path="train.csv"
titanic=pd.read_csv(path)

#2.将PassengerId设置为索引
titanic=titanic.set_index('PassengerId')

#3.绘制一个展示男女乘客比例的扇形图
Male = (titanic.Sex == 'male').sum()
Female = (titanic.Sex == 'female').sum()

proportions = [Male,Female]

plt.pie(proportions, labels=['Male','Female'],shadow=True,
        autopct='%1.1f%%',startangle=90,explode=(0.15,0))
plt.axis('equal')
plt.title('Sex Proportion')
plt.tight_layout()
plt.show()

#4.绘制一个展示船票Fare, 与乘客年龄和性别的散点图
plt.scatter(x='Age',y='Fare', data=titanic)
plt.title('Fare Age Sex')
plt.show()

#5.有多少人生还？
titanic.Survived.sum()

#6.绘制一个展示船票价格的直方图
df = titanic.Fare.sort_values(ascending = False)

plt.hist(df,bins = (np.arange(0,600,10)))
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')
plt.show()
