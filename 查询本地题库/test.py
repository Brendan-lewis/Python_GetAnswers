import  pandas as pd

excel_file = r'副本12.16更新形势与政策必答题库(不完整).xlsx'
data = pd.read_excel(excel_file, index_col='题目')
# 这个的index_col就是index，可以选择任意字段作为索引index，读入数据
print(data.head())