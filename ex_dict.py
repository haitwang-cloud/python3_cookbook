# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:11:00 2016

@author: WangHaitao
"""
"""
en2sp=dict()
print(en2sp)
en2sp={'one':'1','two':'2','three':'3'}
print(en2sp)
val=en2sp.values()
print(val)

def histogram(s):
    d=dict()
    for c in s:
        if c not in d :
            d[c]=1
        else:
            d[c]+=1
    return d
h=histogram('abcdeefghiacbdef')
for key1 in sorted(h):
    print(key1,h[key1])

def invert_dict(d):
    inverse=dict()
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse
h=histogram('abcdeefghiacbdef') 
print(h)
inverse=invert_dict(h)
print(inverse)
"""
#fibonacci 函数用dict()实现
known={0:0,1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res=fibonacci(n-1)+fibonacci(n-2)
    known[n]=res
    return res
print(fibonacci(10))
