from collections import Counter
from operator import itemgetter
from operator import attrgetter
from itertools import groupby
from collections import defaultdict
###命名切片
items=[1,2,3,4,5,6]
a=slice(2,4)
print(items[a])
print(items[2:4])
items[a]=[10,11]
print(items)
del items[a]
print(items)
#可以调用切片的start,stop,step获取信息
print('调用切片的属性')
b=slice(1,10,3)
print('b.start=',b.start)
print('b.stop=',b.stop)
print('b.step=',b.step)
#调用切片的 indices(size) 方法将它映射到一个确定大小的序列上
s='HelloWorld'
print(b.indices(len(s)))
###序列中出现次数最多的元素
print('序列中出现次数最多的元素')
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
print(words)
word_counts=Counter(words)
#出现频率最高的5个单词
print('words中出现频率最高的5个单词')
top_five=word_counts.most_common(5)
print(top_five)
#显示出现某个元素出现的次数
print('eyes=',word_counts['eyes'])
morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print('eyes=',word_counts['eyes'])
count_a=Counter(words)
count_b=Counter(morewords)
print('Counter的数学操作')
print('count_a+count_b===',count_a+count_b)
print('count_a-count_b===',count_a-count_b)
###通过关键字排序一个字典列表
# operator 模块的 itemgetter 函数
#假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_name=sorted(rows,key=itemgetter('fname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
print('rows_by_name',rows_by_name)
print('rows_by_uid',rows_by_uid)
#itemgetter() 函数也支持多个 keys
rows_by_lfname=sorted(rows,key=itemgetter('lname','fname'))
print('rows_by_lfname',rows_by_lfname)
min_uid=min(rows,key=itemgetter('uid'))
max_uid=max(rows,key=itemgetter('uid'))
print('min_uid=',min_uid)
print('max_uid=',max_uid)
### 排序不支持原生比较的对象,使用 operator.attrgetter() 
class User:
    def __init__(self,user_id):
        self.user_id=user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
user=[User(21),User(3),User(99)]
print(user)
print(sorted(user,key=attrgetter('user_id')))
###通过某个字段将记录分组
infor = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
#itertools.groupby() 函数对于这样的数据分组操作非常实用
#在按 date 分组后的数据块上进行迭代
# Sort by the desired field first
infor.sort(key=itemgetter('date'))
# Iterate in groups
#一个非常重要的准备步骤是要根据指定的字段将数据排序。因为 groupby() 仅仅
#检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
for date,item in groupby(infor,key=itemgetter('date')):
    print(date)
    for i in item:
        print(' ',i)
#根据date 字段将数据分组到一个大的数据结构中去，并且允许
#随机访问，那么你最好使用 defaultdict() 来构建一个多值字典
row_by_date=defaultdict(list)
for row in infor:
    row_by_date[row['date']].append(row)
print(row_by_date)
for r in row_by_date['07/02/2012']:
    print(r)