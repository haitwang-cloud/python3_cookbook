import heapq
records=[
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)
for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)
from collections import deque

#在多行上面做简单的文本匹配，并且返回所在行的前N行
def search(lines,pattern,history):
    previous_lines=deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines.append(li)       
if __name__=='__main__':
    with open('D:\python_code\word.txt') as f: 
        for line ,prevlines in search(f,'apple',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='@')
            print('-' * 20)

# 从一个集合中返回最大或者最小的元素列表
#使用heapq模块中的nlagrest（）和nsmallest解决
nums=[1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
portfolio=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','share':200,'price':21.09},
    {'name':'HPQ','share':35,'price':31.75},
    {'name':'yaoo','share':45,'price':15.32},
    {'name':'ACME','share':75,'price':115.65}
]
#python lambda是在python中使用lambda来创建匿名函数
cheap_3=heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
expensive_3=heapq.nlargest(3,portfolio,key=lambda s:s['price'])
print("nlagrest（）和nsmallest")
print(cheap_3)
print(expensive_3)
#堆排序
heapq.heapify(nums)
print("使用堆排序 nums")
print(nums)
#用heapq实现优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index+=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q=PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print("优先级队列",q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())