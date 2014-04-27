'''
Created on 10.04.2014

@author: Friedrich
'''

d = 0

def ProdZ(x,y):
    z = 0
    i = 0
    if (x<0):
        x = (0-x)
        y = (0-y)
    for i in range(0,x):
        z = (z + y)
    return z

def f(x):
    if (x < 0):
        return 0
    elif (x == 0):
        return 1
    else:
        d = ProdZ(f((x-1)),2)
    return d

ausgabe = f(0.3)
print ausgabe