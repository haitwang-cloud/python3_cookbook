# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:56:34 2016

@author: WangHaitao
"""
import time
"""with open('H:\python_code\word.txt') as f:"""
def make_word1():
    t=[]
    f=open('H:\python_code\word.txt')
    for line in f:
        word=line.strip()
        t.append(word)
    return t
def make_word2():
    t=[]
    f=open('H:\python_code\word.txt')
    for line in f:
        word=line.strip()
        t=t+[word]
    return t
start_time=time.time()
t=make_word1()
cost_time=time.time()-start_time

print(len(t))
print(cost_time,'1_sec')

start_time=time.time()
t=make_word2()
cost_time=time.time()-start_time

print(len(t))
print(cost_time,'2_sec')