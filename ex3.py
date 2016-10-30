# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:11:13 2016

@author: WangHaitao
"""

from __future__ import print_function, division

import bisect
import time

def make_word_list():
    word_list = []
    fin = open('H:\python_code\word.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word
def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)

if __name__ == '__main__':
    word_list = make_word_list()
    start_time=time.time()
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])
    cost_time=time.time()-start_time
    print(cost_time)