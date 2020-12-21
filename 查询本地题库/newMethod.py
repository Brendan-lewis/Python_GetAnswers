# coding=utf-8
# Version:python 3.7.0
# Tools:Pycharm 2020.2

import pandas as pd
from pandas import read_excel
import xlrd
_date_ = '2020/12/11 14:13'
_author_ = 'Lewis'

import re
import os
import csv

def GetAnswer(question):
    excel_file = r'副本12.16更新形势与政策必答题库(不完整).xlsx'
    data = pd.read_excel(excel_file, index_col='题目')
    # 这个的index_col就是index，可以选择任意字段作为索引index，读入数据
    answer = data.loc[question]['答案']
    # print(data.loc[question])

    print("答案 : "+str(answer))
    return str(answer)

# name = "选答自测2"  # 这里自己输入文件名字,例如我们要处理ab.txt文件，此处name = "ab", 该写法需要将txt文件和该脚本放在同一目录下
name = "必答自测2"
txtName = name + ".html"
csvName = name + ".csv"

fp = open(txtName, "rb")  # 打开txt文本
a = fp.read()  # 读取txt文本
result = re.findall(r'<h4>([\s\S]*?)</h4>', a.decode('utf-8'))  # 正则匹配
list1 = []  # 该列表用于临时存储字符串
count = 1
for i in result:  # 匹配到的内容逐条提取
    if i != '':  # 过滤空白字符
        print("第 "+str(count)+" 题: "+i)  # 看匹配到的内容
        count += 1
        list1.append(i)  # 将字符串添加到列表再写进去，不然字符会被拆开成一个一个
        # GetAnswer(i)
        answer = GetAnswer(i) # 获取题目的答案
        list1.append(',') # 添加逗号
        list1.append(answer) # 添加答案
        # 下面就是写入csv文件的功能了，newline=''可以避免空行问题
        with open(csvName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list1)
        list1.pop()  # 写入完成要将列表中的字符串删除
        list1.pop()
        list1.pop()