# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 08:38:57 2016

@author: WangHaitao
"""  
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res
print(cumsum([1,2,3,4]))

def middle(t):
    res=t[1:-1]
    return res
print(middle([1,2,3,4,5]))

def chop(t):
    del t[0]
    del t[-1]
t=[1,2,3,4,5]
chop(t)
print(t)
    
def is_sorted(t):
    return t==sorted(t)
print(is_sorted([1,2,3,4,5]))
print(is_sorted(['a','b','c']))

def is_anagram(t1,t2):
    return sorted(t1)==sorted(t2)
print(is_anagram(['a','d','c','b'],['d','c','b','a']))

def has_duplicates(s):
    t=list(s)
    t.sort()
    for i in range(len(t)-1):
        if t[i]==t[i+1]:
            return True
        return False
def main():
    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

if __name__ == '__main__':
    main()