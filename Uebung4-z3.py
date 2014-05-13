'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''
def ListCreate(): #Neue Liste erstellen
  return 2 #leeres Listenelement

def ListGetLength(l): #Anzahl Listenelemente zurückliefern
  count = 0
  merker = l
  while (merker >= 2):
    z1 = binTestBit(merker,1) #Bit auslesen
    merker = divtwo(merker) #Liste verkleinern
    z2 = binTestBit(merker,1) #Naechstes Bit auslesen
    merker = divtwo(merker) #Weiter abschneiden
    if ((z1 == 0) and (z2 == 1)): #Ueberpruefen ob es sich um Trennzeichen handelt
      count = (count + 1) #Wenn ja dann counter um 1 hochzaehlen
  return (count - 1)
  
def ListGetElement(l,i):
  count = 0
  wertigkeit = 1
  summe = 0
  ret = 0
  listLength = ListGetLength(l) #Anzahl der Listenelemente
  if (listLength >= 1): #Wenn elemente vorhanden sind
    merker = l
    while (merker >= 2): #Durch alle Elemente laufen
      z1 = binTestBit(merker,1)
      merker = divtwo(merker)
      z2 = binTestBit(merker,1)
      merker = divtwo(merker)
      if ((z2 == 1) and (z1 == 0)): #Wenn Trennzeichen gefunden wurde
        if (count >= 1): #Es nicht das STart Trennzeichen war
          if (((listLength - i) + 1) == count): #wenn das gewuenschte Element erreicht ist
            ret = summe #Element speichern
        count = (count + 1)
        summe = 0 #Wertigkeit und Summe zuruecksetzen
        wertigkeit = 1
      if ((z1 == 1) and (z2 == 1)): #Ueberpruefen ob 11 gefunden wurde
        summe = (summe + prodZ(z1,wertigkeit)) #Dezimalzahl errechnen
        wertigkeit = (wertigkeit + wertigkeit) #Wertigkeit erhoehen
      if ((z1 == 0) and (z2 == 0)): #Wenn 00 erkant wird nur Wertigkeit erhoehen
        wertigkeit = (wertigkeit + wertigkeit)
  return ret

def ListAppendElement(l,e):
  if(l > 1):
    if ((binTestBit(l, binLength(l)) == 1) and (binTestBit(l, binLength((l-1))) == 0)): #Testen ob es sich um eine Liste handelt
      binNew = 0
      binTmp = 0
      binRet = l
      length = binLength(e) #Laenge des uebergeben Zeichens
      for i in range(0,length): #Jedes Zeichen durchlaufen
        binTmp = binTestBit(e,(length - i)) #Ueberpruefen um welches Zeichen es sich handelt
        if (binTmp == 1): #Wenn Zeichen eine 1
          binNew = (prodZ(binNew,4) + 3) #1 verdoppeln
        else: #Wenn Zeichen 0
          binNew = prodZ(binNew,4) #Zahl um 2 Stellen verschieben
      lengthNew = (binLength(binNew) + 2) #Laenge der Zahl mit Trennzeichen
      if (binNew == 0):
        lengthNew = 4 #Wenn die Uebergebene Zahl eine 0 ist Laenge auf 4 setzen
      binNew = (prodZ(binNew,4) + 2) #Trennzeichen hinzufuegen
      for x in range(0,lengthNew):
        binRet = prodZ(2,binRet) #Liste um laenge der Zahl nach links verschieben
      ret = (binRet + binNew) #Neue Zahl aufaddieren und zurueckgeben
    else:
      ret = -1
  else:
    ret = -1
  return ret
  
## Hilfsmethoden
def prodZ(x,y):
  [i,z] = [0,0] # Initialisierung
  if (x < 0):
    x = (0 - x) # negatives Vorzeichen von x entfernen
    y = (0 - y) # und auf y übertragen
  for i in range(0,x): # x Schleifendurchläufe
    z = (z + y) # y wird x-mal zu z addiert
  return z
  
def divtwo(x): #Zahl durch 2 Teilen
  z = 0
  if (x <= 0):
    z = 0
  if (x > 0):
    while (x >= 2):
      z = (z + 1)
      x = (x - 2)
  return z

def binTestBit(n,stelle): #Gebe Bit an bestimmter Stelle zurueck
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

def binLength(n): #Anzahl an Bits zurueck geben
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

def quicksort(liste):
  if ListGetLength(liste) <= 1:
    return liste
  else:
    return quicksort(filter(lambda x: x < ListGetElement(list, 0), liste[1:])) + \
      [ ListGetElement(list, 0) ] + \
      quicksort(filter(lambda x: x >= ListGetElement(list, 0), liste[1:]))

def main():
  list = ListCreate()
  print(ListAppendElement(1,0))
  list = ListAppendElement(list,1)
  list = ListAppendElement(list,2)
  list = ListAppendElement(list,3)
  return -1