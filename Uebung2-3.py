'''
Created on 27.04.2014

@author: Friedrich
'''

def ListCreate(): #Neue Liste erstellen
    newList = 10 #Leeres Listenelement
    return newList

def division(x,y):
    d = 0
    if (x <= 0):
        d = 0
    if (x > 0):
        while (x >= y):
            d = (d + 1)
            x = (x - y)
    return d

def bin(n): #In bin umrechnen
    count = 0
    zahl = 0
    while (n > 0):
        gesamt = 0
        div = divtwo(n)
        for i in range(0, div):
            gesamt = gesamt + 2
        for e in range(0,count):
            for y in range(0,10):
                zahl = (n - gesamt)
        count = (count + 1)
        n = div
    return zahl

def binLength(n):
    if (n >= 0): #Testen ob zahl Gueltig
        check = 1
        counter = 1
        while (check < n): #Testen ob Check kleiner ist als die uebergebene Zahl
            counter = (counter + 1) #Counter erhoehen
            checkTmp = check
            for i in range(0,10): #Check mal 10
                check = (check + checkTmp)
    return counter #Rueckgabe der Laenge

def binTestBit(n,i):
    if ((n >= 0) and (1 <= i) and (i <= binLength(n))):
        for stelle in range(0,(i-1)):
            n = division(n,10)
        div = division(n,2)
        div = (div + div)
        
        return (n - div)

# def ListGetLength(l):
#     for bit in range(0,binLength(l)):

print binTestBit(10010111,2)