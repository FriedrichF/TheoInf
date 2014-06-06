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
    [Sigma, Z, delta, z0, F] = A     # wobei A ein NEA entsprechend Definition 3.12 ist
    C = [Sigma, Z, delta, z0, Z-F]   # aktzeptierende Zustaende tauschen
    return C

def neaVereinigung(A,B):             # liefert NEA, der die Vereinigung von L(A) und L(B) akzeptiert,
    [ASigma, AZ, Adelta, Az0, AF] = A # wobei A,B NEAs entsprechend Definition 3.12 sind
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma | BSigma
    Z = (1,AZ),(2,BZ),z0                 # Zustaende vereinen und z0 mitaufnehmen

    if((Az0 not in AF) and (Bz0 not in BF)): # Wenn Die Startzustaende keine aktzeptierenden sind
        F = (1,AF),(2,BF)
    else:
        F = (1,AF),(2,BF),z0
        
    delta = (1,Adelta),(2,Bdelta)
    
    
    C = 0;
    return C

def neaKonkatenation(A,B):           # liefert NEA, der L(A)L(B) akzeptiert,
    [ASigma, AZ, Adelta, Az0, AF] = A # wobei A,B NEAs entsprechend Definition 3.12 sind
    [BSigma, BZ, Bdelta, Bz0, BF] = B
    Sigma = ASigma | BSigma
    
    C = 0;
    return C

Z = (1,2,3),(11,22,33)
print(Z[0][0])