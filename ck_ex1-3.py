import math
from itertools import compress
from collections import namedtuple
import os
### 1.16过滤序列元素
#列表推导
mylist=[1,3,-6,7,4,76,34,100]
print([n for n in mylist if n>10])
print([math.sqrt(n) for n in mylist if n > 0])
clip_neg = [n if n > 10 else 0 for n in mylist]
print(clip_neg)
#生成器表达式
pos=(n for n in mylist if n<10)
for x in pos:
    print(x)
#使用内置的filter()函数,filter() 函数反悔了一个迭代器
values = ['1', '2', 'N/A','-3', '-','N/A', '4', 'N/A', '5']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False
ivals=list(filter(is_int,values))
print(ivals)
#过滤工具就是 itertools.compress() ，它以一个 iterable
#对象和一个相对应的 Boolean 选择器序列作为输入参数。然后输出 iterable 对象中对应选择器为 True 的元素。
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
# compress() 也是返回的一个迭代器
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5=[n>5 for n in counts]
print(more5)
more5_add=list(compress(addresses,more5))
for item1 in more5_add:
    print(item1)
###1.17从字典中提取子集
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
p1={key: value for key,value in prices.items() if value >200}
print(p1);
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2={key:value for key,value in prices.items() if key in tech_names}
print(p2)
###1.18映射名称到序列
#collections.namedtuple() 函数通过使用一个普通的元组对象将名称映射到序列元素。
Subscriber=namedtuple('Subscriber',['addr','joined'])
sub=Subscriber('wanghaitao@shu.com','2016-12-28')
print(sub.addr)
print(sub.joined)
# namedtuple跟元组类型是可交换的，支持所有的普通元组操作，比如索引和解压。
addr,joined=sub
print(addr)
print(joined)
#replace() 方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，它是一个非常方便的填充数据的方法
#先创建一个包含缺省值的原型元组，然后使用 replace() 方法创建新的值被更新过的实例
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype=Stock('',0,0.0,None,None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a={'name':'ACME','shares':100,'price':123.76}
dict_to_stock(a)
print(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(b)
###1.19转换并同时计算数据
nums=[1,2,3,4,5,7,8,9,10]
s=sum(x *x for x in nums)
print(s)

files=os.listdir('..')
if any(name.endswith('.py')for name in files):
    print('good')
else:
    print('No python')
# Output a tuple as CSV  
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)