'''
Created on 13.06.2014

@author: Friedrich
'''

def isUnterscheidbar(zi, zj, Sigma, delta, offset, U, F):
    if type(zi) == set:
        zi = list(zi)[0]
        zj = list(zj)[0]
        
    if offset < 0:
        return False
    
    for s in Sigma:
        if zi in F and zj not in F:
            return True
        elif zi not in F and zj in F:
            return True
        
        if zi == zj:
            return False
        
        # Symbol fuer Zustandspaar auslesen.
        # Reihenfolge muss ueberprueft werden!
        try:
            symbol = U[zi,zj]
        except KeyError:
            symbol = U[zj,zi]
            
        if symbol == 'X':
            return True
        else:
            if isUnterscheidbar(delta[zi,s], delta[zj, s], Sigma, delta, offset-1, U, F):
                return True
    

# gibt alle Paare von unterscheidbaren Zustaenden in A zurueck
def deaUnterscheidbareZustaende(A):
    [Sigma, Z, delta, z0, F] = A
    U = dict()
    
    Z = list(Z)
    Sigma = list(Sigma)
    
    set = True
    offset = 1
    
    #Jeden Zustand testen
    for i in range(0,len(Z)):
        for j in range(i+1,len(Z)):
            if Z[i] in F and Z[j] not in F:
                U[Z[i],Z[j]] = 'X'
            elif Z[i] not in F and Z[j] in F:
                U[Z[i],Z[j]] = 'X'
            else:
                U[Z[i],Z[j]] = 'A'   #Wenn es sich um den gleichen Zustand handelt

    #Alle Zustaende testen bis ende erreicht
    print(U)
    while set:
        set = False
        for i in range(0,len(Z)):
            for j in range(1+i,len(Z)):
                if U[Z[i],Z[j]] != 'X':
                    if isUnterscheidbar(Z[i], Z[j], Sigma, delta, offset, U, F): # Ueberpruefen ob zustand unterscheidbar ist
                        set = True
                        U[Z[i],Z[j]] = 'X'
                pass

        offset = offset + 1
    
    # Dictonary in Liste umwandeln
    R = []
    for i in range(0, len(Z)):
        for j in range(1+i,len(Z)):
            if U[Z[i],Z[j]] == 'A':
                R.append((Z[i], Z[j]))
                R.append((Z[j], Z[i]))
                
    print(R)
    return R

def deasAequivalent(A, B):   # prueft, ob DEAs A und B die gleiche Sprache akzeptieren
    [ASigma, AZ, Adelta, Az0, AF] = A
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma & BSigma  # Annahme: ASigma = BSigma
    Z = AZ
    Z |= BZ
    delta = Adelta
    delta.update(Bdelta)
    F = AF
    F |= BF
    
    C = [Sigma, Z, delta, Az0, F]

    return (Az0, Bz0) not in deaUnterscheidbareZustaende(C)

Sigma = {'a', 'b','c'}              # Alphabet
Z = {'Z1','Z2','Z3'}                   # Zustandsmenge
delta2 = {}                      # Ueberfuehrungsfunktion
delta2['Z3','a'] = set(['Z1'])
delta2['Z3','b'] = set(['Z1'])
delta2['Z3','c'] = set(['Z1'])
delta2['Z1','a'] = set(['Z2'])
delta2['Z1','b'] = set(['Z2'])
delta2['Z1','c'] = set(['Z2'])
delta2['Z2','a'] = set(['Z3'])
delta2['Z2','b'] = set(['Z3'])
delta2['Z2','c'] = set(['Z3'])
F = set(['Z1'])
A1 = [Sigma,Z,delta2,'Z1',F]

Sigma = {'a', 'b','c'}   
Z = {'Z5','Z6','Z7','Z8','Z4'}
delta1 = {}                      # Ueberfuehrungsfunktion
delta1['Z5','a'] = set(['Z4'])
delta1['Z5','b'] = set(['Z4'])
delta1['Z5','c'] = set(['Z4'])
delta1['Z6','a'] = set(['Z5'])
delta1['Z6','b'] = set(['Z8'])
delta1['Z6','c'] = set(['Z5'])
delta1['Z7','a'] = set(['Z8'])
delta1['Z7','b'] = set(['Z8'])
delta1['Z7','c'] = set(['Z5'])
delta1['Z8','a'] = set(['Z4'])
delta1['Z8','b'] = set(['Z4'])
delta1['Z8','c'] = set(['Z4'])
delta1['Z4','a'] = set(['Z7'])
delta1['Z4','b'] = set(['Z6'])
delta1['Z4','c'] = set(['Z7'])
F = set(['Z4'])
A2 = [Sigma,Z,delta1,'Z4',F]

print(deasAequivalent(A2,A1))