'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''

def powerset(s):                     # liefert die Potenzmenge der Menge s
    ps = {frozenset()}               # Verwendung von frozenset statt set, da Mengen nur
    for z in s:                      # nichtveraenderbare Objekte enthalten duerfen. Beispiel:
        ps |= {a | {z} for a in ps}  #     falsch:  a = { {1,2}, {4,5} }
    return ps                        #     richtig: a = { frozenset({1,2}), frozenset({4,5}) }

def nea2dea(A):                      # liefert aequivalenten DEA (Potenzmengenkonstruktion)
    [Sigma, Z, delta, z0, F] = A     # A ist ein NEA entsprechend Definition 3.12
    Z1 = powerset(Z)
    delta1 = {}                      # Ueberfuehrungsfunktion
    for S in Z1:                     # Verwendung von frozenset statt set, da Mengen nur
        for a in Sigma:              # nichtveraenderbare Objekte enthalten duerfen. 
            delta1[S,a] = frozenset({s for z in S for s in delta[z, a]})
    F1 = {S for S in Z1 if (S & F) != set()}
    return [Sigma, Z1, delta1, frozenset({z0}), F1]

def neaKomplement(A):                # liefert NEA, der das Komplement von L(A) akzeptiert,
    B = nea2dea(A)                   # DEA erstellen
    [Sigma, Z, delta, z0, F] = B
    
    C = [Sigma, Z, delta, z0, Z-F]   # aktzeptierende Zustaende tauschen
    return C

def neaVereinigung(A,B):             # liefert NEA, der die Vereinigung von L(A) und L(B) akzeptiert,
    [ASigma, AZ, Adelta, Az0, AF] = A # wobei A,B NEAs entsprechend Definition 3.12 sind
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma | BSigma
    
    Z = set([])                     # Zustaende vereinigen
    for z in AZ:
        Z.add('1-' + z)
    for z in BZ:
        Z.add('2-' + z)
    Z.add('z0')

    F = set()                       # Aktzeptierende Zustaende festlegen
    for f in AF:
        F.add('1-' + f)
    for f in BF:
        F.add('2-' + f)
    if((Az0 in AF) or (Bz0 in BF)): # Wenn Die Startzustaende aktzeptierende sind
        F.add('z0')                 # Ist auch der neue Startzustand aktzeptierend
        
    delta = dict()                      # ueberfuehrungsfunktionen zusammenfuehren
    for deltaA in Adelta.keys():
        delta['1-' + deltaA[0],deltaA[1]] = set({'1-' + a for a in Adelta[deltaA[0],deltaA[1]]})
    for deltaB in Bdelta.keys():
        delta[('2-' + deltaB[0]),deltaB[1]] = set({'2-' + a for a in Bdelta[deltaB[0],deltaB[1]]})
        
    for element in Sigma:          # Alle z0 Uebergaenge auf neuen Z0 uebertragen
        delta['z0',element] = set([])
        if(delta['1-' + Az0,element] != set()):
            delta['z0',element] |= (delta['1-' + Az0,element])
        if(delta['2-' + Bz0,element] != set()):
            delta['z0',element] |= (delta['2-' + Bz0,element])
    
    C = [Sigma, Z, delta, 'z0', F];
    return C

def neaKonkatenation(A,B):           # liefert NEA, der L(A)L(B) akzeptiert,
    [ASigma, AZ, Adelta, Az0, AF] = A # wobei A,B NEAs entsprechend Definition 3.12 sind
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma | BSigma
    
    Z = set([])                     # Zustaende vereinigen
    for z in AZ:
        Z.add('1-' + z)
    for z in BZ:
        Z.add('2-' + z)
        
    z0 = '1-' + Az0
    
    F = set()
    for f in BF:
        F.add('2-' + f)
    if Bz0 in BF:                   # Wenn Startzustand des zweiten Automaten aktzeptieren ist, werden die aktzeptierenden des ersten mit genommen
        for f in AF:
            F.add('1-' + f)
    
    delta = {}
    for deltaA in Adelta.keys():
        delta['1-' + deltaA[0],deltaA[1]] = set({'1-' + a for a in Adelta[deltaA[0],deltaA[1]]})
        if deltaA[0] in AF:                                                                     # Wenn der aktuelle Zustand aktzeptierend ist
            delta['1-' + deltaA[0],deltaA[1]] |= ({'2-' + a for a in Bdelta[Bz0,deltaA[1]]})    # wird die Ueberfuehrung zum zweiten Automaten mit uebernommen
    for deltaB in Bdelta.keys():
        delta[('2-' + deltaB[0]),deltaB[1]] = set({'2-' + a for a in Bdelta[deltaB[0],deltaB[1]]})
    
    C = [Sigma, Z, delta, z0, F];
    
    return C

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

delta1 = {}                      # Ueberfuehrungsfunktion
delta1['Z0','a'] = set(['Z1'])
delta1['Z0','b'] = set(['Z0'])
delta1['Z1','b'] = set(['Z2'])
delta1['Z1','a'] = set([])
delta1['Z2','a'] = set([])
delta1['Z2','b'] = set([])
F = set(['Z2','Z0'])
A2 = [Sigma,Z,delta1,'Z0',F]

A1K = neaKonkatenation(A1, A2)
[ASigma, AZ, Adelta, Az0, AF] = A1K
print(A1K)