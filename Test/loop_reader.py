#coding=utf-8
import csv #导入csv 包
#读取本地CSV 文件
my_file='test1data.csv'
#for python2
data=csv.reader(file(my_file,'rb'))
#循环输出每一行信息
for user in data:
         print(user)
         print(user[2])
#for python3
#with open(my_file, newline='') as f:
#    data = csv.reader(f)
#    for user in data:
#        print(user[1])
