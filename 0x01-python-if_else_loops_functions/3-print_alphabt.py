#!/usr/bin/python3
"""
Created on Wed Jun  1 00:18:36 2022

@author: Teklewoyn
"""
a = range(97, 123)
b = ''
for x in a:
    if x == 101:
        continue
    elif x == 113:
        continue
    b += chr(x)
print(b.format())
