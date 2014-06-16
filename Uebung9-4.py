'''
Created on 13.06.2014

@author: Friedrich
'''

# gibt alle Paare von unterscheidbaren Zustaenden in A zurueck
def deaUnterscheidbareZustaende(A):
    [Sigma, Z, delta, z0, F] = A
    U = [[0 for x in Z] for x in Z]
    
    Z = list(Z)
    Sigma = list(Sigma)
    
    set = True
    offset = 1
    
    #Jeden Zustand testen
    for i in range(0,len(Z)):
        for j in range(0,len(Z)):
            if Z[i] in F and Z[j] not in F:
                set = True
                U[i][j] = 'X'
            if Z[i] not in F and Z[j] in F:
                U[i][j] = 'X'
    
    #Alle Zustaende testen bis ende erreicht
    while set:
        set = False
        for s in Sigma:
            for i in range(0,len(Z)):
                for j in range(0,len(Z)):
                    zi = Z[i]
                    zj = Z[j]
                    for off in range(0,offset):
                        zi = delta[zi,s]
                        print(zi)
                        zj = delta[zj,s]
                    if zi in F and zj not in F:
                        set = True
                        U[i][j] = 'X'
                    if zi not in F and zj in F:
                        U[i][j] = 'X'
                        set = True
        offset = offset + 1
    print(U)
    return U

def deasAequivalent(A, B):   # prueft, ob DEAs A und B die gleiche Sprache akzeptieren
    [ASigma, AZ, Adelta, Az0, AF] = A
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma & BSigma  # Annahme: ASigma = BSigma
    Z = AZ
    Z |= BZ
    delta = Adelta
    delta |= Bdelta
    F = AF & BF
    
    C = [Sigma, Z, delta, Az0, F]
    print(A)
    print(B)
    print(C)
    return C
    #return {Az0, Bz0} not in deaUnterscheidbareZustaende(C)

Sigma = {'a', 'b'}              # Alphabet
Z = {'Z0','Z1','Z2'}                   # Zustandsmenge
delta2 = {}                      # Ueberfuehrungsfunktion
delta2['Z0','a'] = set(['Z1'])
delta2['Z0','b'] = set([])
delta2['Z1','a'] = set(['Z1'])
delta2['Z1','b'] = set(['Z2'])
delta2['Z2','b'] = set([])
delta2['Z2','a'] = set([])
F = set(['Z2'])
A1 = [Sigma,Z,delta2,'Z0',F]

Z = {'Z10','Z11','Z12'}
delta1 = {}                      # Ueberfuehrungsfunktion
delta1['Z10','a'] = set(['Z11'])
delta1['Z10','b'] = set(['Z10'])
delta1['Z11','b'] = set(['Z12'])
delta1['Z11','a'] = set([])
delta1['Z12','a'] = set([])
delta1['Z12','b'] = set([])
F = set(['Z12','Z10'])
A2 = [Sigma,Z,delta1,'Z10',F]

deaUnterscheidbareZustaende(A1)