import re
from calendar import month_abbr
###字符串匹配和搜索
#基本的str.find(),str.startswith().str.endswith()
text_list='apple,banana,orange,juice,pear,pineapple,watermelon'
print(text_list.startswith('apple'))
print(text_list.endswith('lon'))
print(text_list.find('le'))
#复杂的需要使用正则表达式和re模块
text1='12/01/2016'
text2 = 'Nov 27, 2012'
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes match')
else:
    print('no match')
if re.match(r'\d+/\d+/\d+',text2):
    print('yes match')
else:
    print('no match')
#使用同一个模式去多次匹配，将模式字符串预编译模式对象
datepat=re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes match')
else:
    print('no match')
if datepat.match(text2):
    print('yes match')
else:
    print('no match')
text_list1 = 'Today is 12/25/2016. PyCon starts 1/12/2016.'
print(datepat.findall(text_list1))
#利用括号去捕获分组
print('用括号去捕获分组')
datepat_new=re.compile(r'(\d+)/(\d+)/(\d+)')
m=datepat_new.match('12/25/2016')
print('m.group(0):',m.group(0))
print('m.group(1):',m.group(1))
print('m.group(2):',m.group(2))
print('m.group(3):',m.group(3))
print('m.groups():',m.groups())
month,day,year=m.groups()
print(month,day,year)
#finditer()以迭代方式返回匹配
text = 'Today is 12/25/2016. PyCon starts 1/12/2016.'
for m1 in datepat_new.finditer(text):
    print(m1.groups())
#如果你想精确匹配，确保你的正则表达式以 $ 结尾
###2.5字符串搜索和替换
#简单的模式
text_list='apple,banana,orange,juice,pear,pineapple,watermelon'
print('replace banana@',text_list.replace('banana','milk'))
print(text_list)
#复杂的模式,使用re.sub(),将形式为 11/27/2012 的日期字符串改成 2012-11-27
text = 'Today is 12/25/2016. PyCon starts 1/12/2016.'
print('sub使用之前',text)
#反斜杠数字比如 \3 指向前面模式的捕获组号。
print('sub使用之后',re.sub(r'(\d+)/(\d+)/(\d+)',r'\1-\2-\3',text))
print('编译之后在使用',datepat_new.sub(r'\1-\2-\3',text))
#对于更加复杂的替换，可以传递一个替换回调函数来代替
def change_date(m):
    mon_name=month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
print('使用替换回调函数',datepat_new.sub(change_date,text))
#使用subn（）查询替换了多少次
newtext,n=datepat_new.subn(r'\1-\2-\3',text)
print('替换次数=',n)
###2.6字符串忽略大小写的搜索替换
text = 'UPPER PYTHON, lower python, Mixed Python'
print('忽略大小写的搜索',re.findall('python',text,flags=re.IGNORECASE))
print('忽略大小写的替换',re.sub('python','snake',text,flags=re.IGNORECASE))
#替换字符串跟匹配的大小写一致
def matchchase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
#matchcase('snake') 返回了一个回调函数 (参数必须是 match 对象)
print(re.sub('python',matchchase('snake'),text,flags=re.IGNORECASE))
###2.7最短匹配模式
#点 (.) 匹配除了换行外的任何字符。
#通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
str_pat=re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print("贪婪搜索",str_pat.findall(text2))
str_pat_new=re.compile(r'\"(.*?)\"')
print("非贪婪搜索",str_pat_new.findall(text2))
###2.8多行匹配
#点 (.) 不能匹配换行符
comment=re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2='''/* this is 
a comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))
comment_new=re.compile(r'/\*((?:.|\n)*?)\*/')
 #(?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
print('添加了对换行的支持',comment_new.findall(text2))