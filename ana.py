# coding=utf-8
# Version:python 3.7.0
# Tools:Pycharm 2020.2
import json
import urllib.parse
import urllib.request

_date_ = '2020/12/11 14:13'
_author_ = 'Lewis'

import re
import os
import csv

def GetAnswer(question):
    values={}
    values['question']  = question
    url =  "https://user.fm210.cn/api/wk?token="
    data = urllib.parse.urlencode(values)

    reqUrl = url + '&' + data
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=reqUrl, headers=headers)
    response = urllib.request.urlopen(req)
    # answer = json.loads(response.text).get('da')
    # answer = answer.encode('utf8').decode('unicode_escape')
    # print(answer)
    the_page = response.read()

    the_page.decode("unicode_escape")
    jsonData = json.loads(the_page)
    # 中文编码格式打印数据
    answer = jsonData['da']
    print("答案 : "+answer)
    return answer

# name = "选答自测2"  # 这里自己输入文件名字,例如我们要处理ab.txt文件，此处name = "ab", 该写法需要将txt文件和该脚本放在同一目录下
name = "必答自测1"
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