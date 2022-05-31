#!/usr/bin/python3
"""
Created on Wed Jun  1 02:04:02 2022

@author: Vineyard22
"""
num = range(100)
for x in num:
    print('%02d'.foramt() % (x), end='')
    if x != 99:
        print(end=', '.format())
