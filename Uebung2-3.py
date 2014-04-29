def ListCreate(): #Neue Liste erstellen
  return 2 #leeres Listenelement

def ListGetLength(l): #Anzahl Listenelemente zurückliefern
  count = 0
  merker = l
  while (merker >= 2):
    z1 = binTestBit(merker,1)
    merker = divtwo(merker)
    z2 = binTestBit(merker,1)
    merker = divtwo(merker)
    if ((z1 == 0) and (z2 == 1)):
      count = (count + 1)
  return (count - 1)
  
def ListGetElement(l,i):
  count = 0
  wertigkeit = 1
  summe = 0
  ret = 0
  listLength = ListGetLength(l)
  if (listLength >= 1):
    merker = l
    while (merker >= 2):
      z1 = binTestBit(merker,1)
      merker = divtwo(merker)
      z2 = binTestBit(merker,1)
      merker = divtwo(merker)
      if ((z2 == 1) and (z1 == 0)):
        if (count >= 1):
          if (((listLength - i) + 1) == count):
            ret = summe
        count = (count + 1)
        summe = 0
        wertigkeit = 1
      if ((z1 == 1) and (z2 == 1)):
        summe = (summe + prodZ(z1,wertigkeit))
        wertigkeit = (wertigkeit + wertigkeit)
      if ((z1 == 0) and (z2 == 0)):
        wertigkeit = (wertigkeit + wertigkeit)
  return ret

def ListAppendElement(l,e):
  binNew = 0
  binTmp = 0
  binRet = l
  length = binLength(e)
  for i in range(0,length):
    binTmp = binTestBit(e,(length - i))
    if (binTmp == 1):
      binNew = (prodZ(binNew,4) + 3)
    else:
      binNew = prodZ(binNew,4)
  lengthNew = (binLength(binNew) + 2)
  if (binNew == 0):
    lengthNew = 4
  binNew = (prodZ(binNew,4) + 2)
  for x in range(0,lengthNew):
    binRet = prodZ(2,binRet)
  return (binRet + binNew)
  
## Hilfsmethoden
def prodZ(x,y):
  [i,z] = [0,0] # Initialisierung
  if (x < 0):
    x = (0 - x) # negatives Vorzeichen von x entfernen
    y = (0 - y) # und auf y übertragen
  for i in range(0,x): # x Schleifendurchläufe
    z = (z + y) # y wird x-mal zu z addiert
  return z
  
def divtwo(x):
  z = 0
  if (x <= 0):
    z = 0
  if (x > 0):
    while (x >= 2):
      z = (z + 1)
      x = (x - 2)
  return z

def binTestBit(n,stelle):
  ret = 0
  iStelle = 0
  if (n <= 0):
    ret = 0
  while ((n > 0) and (stelle > iStelle)):
    iStelle = (iStelle + 1)
    p = 0
    zahl = divtwo(n)
    for i in range(0, zahl):
      p = (p + 2)
    ret = (n - p)
    n = zahl
  return ret

def binLength(n):
  ret = 0
  iStelle = 0
  if (n < 0):
    iStelle = 0
  if (n == 0):
    iStelle = 1
  while (n > 0):
    iStelle = (iStelle + 1)
    n = divtwo(n)
  return iStelle

def main():
  list = ListCreate()
  list = ListAppendElement(list,0)
  list = ListAppendElement(list,1)
  list = ListAppendElement(list,2)
  list = ListAppendElement(list,3)
  print (ListGetElement(list,4))
  return -1