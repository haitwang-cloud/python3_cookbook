import os
import types
from collections import ChainMap
print(os.getcwd())
py_files=os.listdir(os.getcwd())
print(py_files)
if any(name.endswith('.py') for name in py_files):
    print('you have python!!!!!!!!!!!!')
else:
    print('no python ')

###1.20合并多个字典或映射
#利用ChainMap实现
a={'x1':1,'x2':'hey,there'}
b={'x3':3,'x4':4}
c={'x5':5,'x6':6}
dict_s=ChainMap(a,b,c)
print("dict_s",dict_s['x2'])
print('len(dict_s)=',len(dict_s))
print(list(dict_s.keys()))
print(list(dict_s.values()))
#对于字典的更新或删除操作总是影响的是列表中第一个字典
del dict_s['x1']
print('dict_s',type(dict_s),dict_s)
#测试用
#del dict_s['x3']
values=ChainMap()
values['x']=1
values=values.new_child()
values['x']=2
values=values.new_child()
values['x']=3
print(type(values),values)
#可以利用update()将两个字典合并
a={'x':1,'z':3}
b={'y':2,'z':4}
merged=dict(b)
merged.update(a)
print(type(merged),merged)
c={'x':1,'z':3}
d={'y':2,'z':4}
merged1=ChainMap(c,d)
print(type(merged1),merged1)