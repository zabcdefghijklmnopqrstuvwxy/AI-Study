#练习八：创建数据库
import pandas as pd 
#1.创建一个数据字典
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }

#2.将数据字典存为一个名叫pokemon的数据框中
pokemon=pd.DataFrame(raw_data)

#3.数据框的列排序是字母顺序，请重新修改为name, type, hp, evolution, pokedex这个顺序
pokemon=pokemon[['name','type','hp','evolution','pokedex']]

#4.添加一个列place['park','street','lake','forest']
pokemon['place'] = ['park','street','lake','forest']

#5.查看每个列的数据类型
pokemon.dtypes