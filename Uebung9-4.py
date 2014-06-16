'''
Created on 13.06.2014

@author: Friedrich
'''

# gibt alle Paare von unterscheidbaren Zustaenden in A zurueck
def deaUnterscheidbareZustaende(A):
    [Sigma, Z, delta, z0, F] = A
    U = dict()
    
    Z = list(Z)
    print(Z)
    Sigma = list(Sigma)
    
    set = True
    offset = 1
    
    #Jeden Zustand testen
    for i in range(0,len(Z)):
        for j in range(0+i+1,len(Z)):
            if Z[i] in F and Z[j] not in F:
                U[Z[i],Z[j]] = 'X'
            elif Z[i] not in F and Z[j] in F:
                U[Z[i],Z[j]] = 'X'
            else:
                U[Z[i],Z[j]] = 'A'   #Wenn es sich um den gleichen Zustand handelt

    #Alle Zustaende testen bis ende erreicht
    while set:
        set = False
        for s in Sigma:
            for i in range(0,len(Z)):
                for j in range(0+1+i,len(Z)):
                    zi = Z[i]
                    zj = Z[j]
                    
                    zi_tmp = zi
                    zj_tmp = zj
                    
                    if U[zi,zj] == 'X':    #Wenn der Zustand schon Unterscheidbar ist, dann weiter
                        break
                    
                    for off in range(0,offset):
                        zi = delta[zi,s]
                        zj = delta[zj,s]
                        
                    if (list(zi)[0] == list(zj)[0]):
                        break
                        
                    # Symbol fuer Zustandspaar auslesen.
                    # Reihenfolge muss ueberprueft werden!
                    try:
                        symbol = U[(list(zi)[0],list(zj)[0])]
                    except KeyError:
                        symbol = U[(list(zj)[0],list(zi)[0])]

                    if symbol == 'X':
                        set = True
                        U[zi_tmp,zj_tmp] = 'X'

        offset = offset + 1
    print(U)
    
    # Dictonary in Liste umwandeln
    R = []
    for i in range(0, len(Z)):
        for j in range(0+1+i,len(Z)):
            if U[Z[i],Z[j]] == 'A':
                R.append((Z[i], Z[j]))
                R.append((Z[j], Z[i]))
    return U

def deasAequivalent(A, B):   # prueft, ob DEAs A und B die gleiche Sprache akzeptieren
    [ASigma, AZ, Adelta, Az0, AF] = A
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma & BSigma  # Annahme: ASigma = BSigma
    Z = AZ
    Z |= BZ
    delta = Adelta
    delta.update(Bdelta)
    print(delta)
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