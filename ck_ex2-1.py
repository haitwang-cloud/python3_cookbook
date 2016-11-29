#####第四章的内容：字符串和文本
#####重点是文本的操作处理，比如提取字符串，搜索，替换以及解析等
import re
import os
from urllib.request import urlopen
from fnmatch import fnmatch,fnmatchcase
###2.1 使用多个界定符分割字符串
#line的split()方法适合于简单的字符串分割情形,复杂的使用re.split方法
line='apple banana;pear,strawberry,orange,bee'
line_new=re.split(r'[;,\s]\s*',line)
print(line_new)
line_new_2=re.split(r'(;|,|\s)\s*',line)
print(line_new_2)
values=line_new_2[::2]
###字符串开头或结尾匹配
print(os.getcwd())
file_name='h:\python\python_code\ex_dict.py'
print(file_name.endswith('.py'))
print(file_name.endswith('file'))
url = 'http://www.python.org'
print(url.startswith('http:'))
py_files=os.listdir(os.getcwd())
#print(py_files)
all_files=[name for name in py_files if name.endswith(('.py','.txt'))]
print(any(name.endswith('.py') for name in py_files))
print(all_files)

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
read_data('https://github.com/Rochester-NRT/RocAlphaGo/wiki/02.-Code')
###使用shell通配符匹配字符串
#使用fnmatch中的fnmatch()和fnmatchcase()
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
name_list=[name for name in names if fnmatch(name,'Dat*.csv')]
print(name_list)
#fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来匹配模式。
print(fnmatch('foo.txt','*.TXT'))
print(fnmatch('foo.txt','*.Txt'))
#fnmatchcase严格区分大小写
print(fnmatchcase('foo.txt','*.TXT'))
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
addr_list=[addr for addr in addresses if fnmatchcase(addr,'*ST')]
print(addr_list)
addr_list_1=[addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9]*CLARK*')]
print(addr_list_1)
#2.4字符串匹配和搜索