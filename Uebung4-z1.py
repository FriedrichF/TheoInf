'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''
def prim(n):
    return primRek(n,0,2)

def primRek(n,k,m):
    if (n > k):
        m = (m + 1)
        if (teil(m) == 2):
            k = (k + 1)
        m = primNeu(n,k,m)
    return m

def teil(x):
    k=0 # Zaehler auf 0
    for i in range(1,(x + 1)): # i = 1, ..., x
        if (modZ(x,i) == 0):
            k = (k + 1) # Zaehler erhoehen
    return k

def modZ(x,y):
    return (x - prodZ(y,divZ(x,y)))

def prodZ(x,y):
    [i,z] = [0,0] # Initialisierung
    if (x < 0):
        x = (0 - x) # negatives Vorzeichen von x entfernen
        y = (0 - y) # und auf y uebertragen
    for i in range(0,x): # x Schleifendurchlaeufe
        z = (z + y) # y wird x-mal zu z addiert
    return z

def divZ(x,y):
    if (y != 0): # nicht definierte Rueckgabe, falls y=0
        if (y < 0):
            y = (0 - y) # neg. Vorzeichen von y entfernen
            x = (0 - x) # und auf x uebertragen
        z = 0
        if (x < 0): # z = min(0,x)
            z = x
            # hier gilt y>0 und y*z <= x
        while (prodZ(y,z) <= x): # suche groesstes z mit y*z<=x
            z = (z + 1)
        z = (z - 1) # Korrektur, weil zu weit gezaehlt
    return z

print(prim(100))
print (primNeu(100,0,2))