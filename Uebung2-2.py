'''
Created on 28.04.2014

@author: Friedrich
'''
def f6(x):
    i =0
    y=1
    z=1
    while (z<x):
        i=(i+1)
        z=(z+y)
        y=(y+y)
    return i

print f6(33)