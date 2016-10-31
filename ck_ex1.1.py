from collections import defaultdict
from collections import OrderedDict

#multidict 一个键对应多个值
print('一个键对应多个值')
d={
    'a':[1,2,3],
    'b':[4,5]
}
e={
    'a':{1,2,3},
    'b':{4,5}
}
print(d,e)

d1=defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['a'].append(4)
print(d1)

#字典排序，迭代或序列化这个字典的时候能够控制元素的顺序
#一个 OrderedDict 的大小是一个普通字典的两倍
def ordered_dict():
    d=OrderedDict()
    #d=dict()
    d['foo']=1
    d['bar']=2
    d['spam']=3
    d['grok']=4
    for key in d:
        print(key,d[key])
print("字典排序")        
ordered_dict()
#在数据字典中执行一些计算操作 (比如求最小值、最大值、排序等等)
prices={
    'acme':45.32,
    'aapl':612.78,
    'ibm':205.21,
    'hpq':37.29,
    'FB':10.73
}
#zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表
print("在数据字典中执行一些计算操作 (比如求最小值、最大值、排序等等)")
#当比较两个元组的时候，值会先进行比较，然后才是键。
min_price=min(zip(prices.values(),prices.keys()))
max_price=max(zip(prices.values(),prices.keys()))
prices_sorted=sorted(zip(prices.values(),prices.keys()))
print("min_price=",min_price,"max_price",max_price,"prices_sorted",prices_sorted[::-1])

#寻找两个字典的相同点
a={
    'x':1,
    'y':2,
    'z':3
}
b={
    'w':10,
    'x':11,
    'y':2
}
# Find keys in common
print(a.keys()&b.keys())
#Find keys in a that are not in b
print(a.keys()-b.keys())
# Find (key,value) pairs in common
print(a.items()&b.items())
# Make a new dictionary with certain keys removed
c={key:a[key] for key in a.keys()-{'z','w'}}
print('c=',c)
# 删除序列相同元素并保持顺序
#序列值是hashable类型
def dedupe_1(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a=[1,5,2,1,9,1,5,10]
print("可哈希类型")
print(list(dedupe_1(a)))
def dedupe_2(items,key=None):
    seen=set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
b=[{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':1,'y':4}]
print("不可哈希类型")
print(list(dedupe_2(b,key=lambda d:(d['x'],d['y'])))) 
