'''
Created on 06.05.2014

@author: Friedrich
'''
def DyadicRepresentation(x):
    rest = 0
    i = 0
    list = []
    while (x > 0):
        rest = x%2
        if (rest == 0):
            rest = 2
        x -= rest
        x /= 2
        list += [0]
        list[i] += rest
        i += 1
    return list[::-1] #Liste rueckwaerts zurueck geben

def Number(l):
    dez = 0
    list = l[::-1]
    wertigkeit = 1
    for i in range(0,len(l)):
        dez += wertigkeit * list[i]
        wertigkeit *= 2
    return dez

def main(x):
    z = 0
    b1 = DyadicRepresentation(x) + [0]
    b2 = [0]
    h1 = h2 = 0
    while(z != 1):
        if ((z == 0) and (b1[h1] == 1) and (b2[h2] == 0)):
            b1[h1] = 1
            b2[h2] = 1
            h1 += 1
            b2 = [0] + b2
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 0) and (b1[h1] == 2) and (b2[h2] == 0)):
            b1[h1] = 2
            b2[h2] = 2
            h1 += 1
            b2 = [0] + b2
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 0) and (b1[h1] == 0) and (b2[h2] == 0)):
            z = 2
            b1[h1] = 0
            b2[h2] = 0
            h2 += 1
            if (h2 >= len(b2)):
                b2 = b2 + [0]
        if ((z == 2) and (b1[h1] == 0) and (b2[h2] == 1)):
            b1[h1] = 1
            b2[h2] = 0
            h2 += 1
            h1 += 1
            if (h2 >= len(b2)):
                b2 = b2 + [0]
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 2) and (b1[h1] == 0) and (b2[h2] == 2)):
            z = 3
            b1[h1] = 2
            b2[h2] = 0
            h2 += 1
            h1 += 1
            if (h2 >= len(b2)):
                b2 = b2 + [0]
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 2) and (b1[h1] == 0) and (b2[h2] == 0)):
            z = 1
        if ((z == 3) and (b1[h1] == 0) and (b2[h2] == 1)):
            z = 3
            b1[h1] = 1
            b2[h2] = 0
            h2 += 1
            h1 += 1
            if (h2 >= len(b2)):
                b2 = b2 + [0]
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 3) and (b1[h1] == 0) and (b2[h2] == 2)):
            z = 1
            b1[h1] = 0
            b2[h2] = 0
            h2 += 1
            h1 += 1
            if (h2 >= len(b2)):
                b2 = b2 + [0]
            if (h1 >= len(b1)):
                b1 = b1 + [0]
        if ((z == 3) and (b1[h1] == 0) and (b2[h2] == 0)):
            z = 1
            
    del b1[len(b1)-1] #letzte 0 entfernen

    for i in range(0,len(b1)): #Testen ob eine 0 vorhanden ist und damit mehrere Woerter
        if (b1[i] == 0):
            return 0
    
    y = Number(b1)
    return y

print (main(23))