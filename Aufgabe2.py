'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''
def prodZ(x,y):
    z = 0
    i = 0
    if (x<0):
        x = (0-x)
        y = (0-y)
    for i in range(0,x):
        z = (z + y)
    return z

def divZNeu(x,y):
    i = 0
    minus = 0
    if (y != 0):
        if ((y < 0) and (not(x < 0))):
            y = (0-y)
            minus = 1
        if ((x < 0) and (not(y < 0))):
            x = (0-x)
            minus = 1
        if ((x < 0) and (y < 0)):
            x = (0-x)
            y = (0-y)
        while (x>=y):
            i = (i + 1)
            x = (x-y)
    if(minus == 1):
        ret = (0-i)
    else:
        ret = i
    return ret