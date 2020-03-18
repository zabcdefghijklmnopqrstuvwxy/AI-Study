练习五：合并
1. 导入必要的库

2.按照如下的元数据内容创建数据框

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

3.将上述的数据框分别命名为data1, data2, data3

4.将data1和data2两个数据框按照行的维度进行合并，命名为all_data

5.将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col

6.打印data3

7.按照subject_id的值对all_data和data3作合并

8.对data1和data2按照subject_id作连接

9.找到 data1 和 data2 合并之后的所有匹配结果

