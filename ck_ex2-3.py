import unicodedata
import re
import sys
###2.9将Unicode文本标准化
s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'
print('unicodedata标准化之前',s1==s2,s1,s2)
#使用unicodedata模块能将文本标准化,NFC 表示字符应该是整体组成
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
print('unicodedata NFC标准化之后',t1==t2,t1,t2)
#NFD 表示字符应该分解为多个组合字符表示
t3=unicodedata.normalize('NFD',s1)
t4=unicodedata.normalize('NFD',s2)
print('unicodedata NFD标准化之后',t3==t4,t3,t4)
###2.10在正则式中使用 Unicode
import re
num=re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))
###2.11删除字符串中不需要的字符
#strip() 方法能用于删除开始或结尾的字符
s1='hello@@ ##world'
s2=' hello world \n '
#s.strip方法只能用于删除开始或结尾的字符
#lstrip从左开始执行删除操作，rstrip从右开始
print(s2,s2.strip())
print(s1.lstrip('@'))
print(s1.rstrip('#'))
#处理中间的空格,使用 replace() 方法或者是用正则表达式替换
print('replace方法',s1.replace('@',''))
print('replace方法',s1.replace('#',''))
#从文件中读取多行数据。
print('从文件中读取多行数据。')
with open('H:\python\python_code\word1.txt') as f:
    lines=(line.strip() for line in f)
    for line in lines:
        print(line)
###2.12审查清理文本字符串
#例如清除整个区间上的字符
print('审查清理文本字符串')
"""通过使用 dict.fromkeys() 方法构造一个字典，每个 Unicode 和音
符作为键，对于的值全部为 None 。
然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。然后再
调用 translate 函数删除所有重音符。同样的技术也可以被用来删除其他类型的字符
(比如控制字符等)。"""
s = 'pýtĥöñ\x0cis\tawesome\r\n'
print(s)
remap={
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):None
}
a=s.translate(remap)
print(a)
#接着让我们删除所有的和音符
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))
#使用replace方法较快的执行
def clean_spaces(s):
    s=s.replace('\r',' ')
    s=s.replace('\t',' ')
    s=s.replace('\f',' ')
    return s
print(clean_spaces(s))
###字符串对齐
#ljust,rjust和center
text=' @Hello World@ '
print(text)
print(text.ljust(20,'='))
print(text.rjust(20,'='))
print(text.center(20,'='))
#函数 format() 同样可以用来很容易的对齐字符串。你要做的就是使用 <,> 或者ˆ 字符后面紧跟一个指定的宽度。
print('format >20',format(text,'>20'))
print('format <20',format(text,'<20'))
print('format ^20',format(text,'^20s'))
#如果你想指定一个非空格的填充字符，将它写到对齐字符的前面即可
print('format =>20',format(text,'=>20s'))
print('format *^',format(text,'*^20s'))
#format也可以用来格式化任何值
###2.14 合并拼接字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(parts)
print(' '.join(parts))
print(','.join(parts))
print('@ '.join(parts))
data=['ACME',50,91.1]
print('_'.join(str(d) for d in data))
