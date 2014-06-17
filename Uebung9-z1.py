'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''

def getZustandIndex(z, unterschZ):  # sucht einen Zustand in einer Liste und gibt Index zurueck
    Aequi = []
    i = -1
    for a in unterschZ:
        i = i + 1
        if type(a) == tuple:    # Wenn es sich um ein Tupel handelt wird dieses weiter aufgeteilt
            for b in a:
                if b == z:
                    return i
        else:
            if a == z:
                return i
    return -1

def isUnterscheidbar(zi, zj, Sigma, delta, offset, U, F): # Ueberprueft ob zustandspaar Unterscheidbar ist
    if type(zi) == set:
        zi = list(zi)[0]
        zj = list(zj)[0]
        
    if offset < 0: # Wenn tiefe erreicht ist handelt es sich um einen Aequivalentes Zustandspaar
        return False
    
    for s in Sigma:        
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
    
    #Jeden Zustand testen ob unterscheidbar
    for i in range(0,len(Z)):
        for j in range(i+1,len(Z)):
            if Z[i] in F and Z[j] not in F:
                U[Z[i],Z[j]] = 'X'
            elif Z[i] not in F and Z[j] in F:
                U[Z[i],Z[j]] = 'X'
            else:
                U[Z[i],Z[j]] = 'A'   #Wenn es sich um den gleichen Zustand handelt

    #Alle Zustaende testen bis ende erreicht
    while set:
        set = False
        for i in range(0,len(Z)):
            for j in range(1+i,len(Z)):
                if U[Z[i],Z[j]] != 'X':
                    if isUnterscheidbar(Z[i], Z[j], Sigma, delta, offset, U, F): # Ueberpruefen ob zustand unterscheidbar ist
                        set = True
                        U[Z[i],Z[j]] = 'X'
        offset = offset + 1
    
    # Dictonary in Liste umwandeln
    R = []
    for i in range(0, len(Z)):
        for j in range(1+i,len(Z)):
            if U[Z[i],Z[j]] == 'A':
                indexI = getZustandIndex(Z[i], R)
                indexJ = getZustandIndex(Z[j], R)
                
                if indexI != -1:
                    if not Z[j] in R[indexI]:
                        R[indexI] = R[indexI] + (Z[j],)
                elif indexJ != -1:
                    if not Z[i] in R[indexJ]:
                        R[indexJ] = R[indexJ] + (Z[i],)
                else:
                    R.append((Z[i], Z[j]))
                
    return R
            
def getErreichbareZ(z0, Sigma, delta):  # Liefert alle erreichbaren Zustaende zurueck
    R = [z0]
    elementZExist = True
    i = 0
    
    while elementZExist:
        elementZExist = False
        z = list(R)[i]
        for s in Sigma:
            if list(delta[z,s])[0] not in R:
                R.append(list(delta[z,s])[0])
                elementZExist = True
        i = i + 1
    return R

def miniDea(A):
    [Sigma, Z, delta, z0, F] = A
    Z = getErreichbareZ(z0, Sigma, delta)
    A = [Sigma, Z, delta, z0, F]
    unterschZ = deaUnterscheidbareZustaende(A)
    
    # Fuege fehlende Zustaende zu den Aequivalenten hinzu
    for z in Z:
        if getZustandIndex(z, unterschZ) == -1:
            unterschZ.append(z)    
    
    # Jeder Zustand der einen alten aktzeptierenden Zustand enthaelt wird aktzeptierend
    F_mini = set()
    for f in F:
        index = getZustandIndex(f, unterschZ)
        if index != -1:
            F_mini.add(unterschZ[index])
    
    # Uebergangsfunktion erzeugen
    delta_mini = {}
    for z in Z:
        for s in Sigma:
            index = getZustandIndex(z, unterschZ)   # Zustand in neuen Zustaenden suchen
            index_to = getZustandIndex(list(delta[z,s])[0], unterschZ)
            delta_mini[unterschZ[index],s] = set([unterschZ[index_to]])
    
    Z_mini = set(unterschZ)  # Neue Zustandsmenge
    
    A_mini = [Sigma, Z_mini, delta_mini, z0, F_mini]
    return A_mini

Sigma = {'a', 'b'}   
Z = {'Z5','Z0','Z2','Z3','Z4','Z1'}
delta1 = {}                      # Ueberfuehrungsfunktion
delta1['Z5','a'] = set(['Z4'])
delta1['Z5','b'] = set(['Z0'])
delta1['Z0','a'] = set(['Z4'])
delta1['Z0','b'] = set(['Z1'])
delta1['Z2','a'] = set(['Z5'])
delta1['Z2','b'] = set(['Z0'])
delta1['Z3','a'] = set(['Z2'])
delta1['Z3','b'] = set(['Z3'])
delta1['Z4','a'] = set(['Z2'])
delta1['Z4','b'] = set(['Z0'])
delta1['Z1','a'] = set(['Z5'])
delta1['Z1','b'] = set(['Z3'])
F = set(['Z1', 'Z3'])
A2 = [Sigma,Z,delta1,'Z0',F]
print(A2)
print(miniDea(A2))
