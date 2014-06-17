'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''

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
                pass

        offset = offset + 1
    
    # Dictonary in Liste umwandeln
    R = []
    for i in range(0, len(Z)):
        for j in range(1+i,len(Z)):
            if U[Z[i],Z[j]] == 'A':
                R.append((Z[i], Z[j]))
                
    return R
            
def getErreichbareZ(z0, Sigma, delta):
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

def getZustandIndex(z, unterschZ):
    Aequi = []
    i = -1
    for a in unterschZ:
        i = i + 1
        if type(a) == tuple:
            for b in a:
                if b == z:
                    return i
        else:
            if b == z:
                return i
    return -1

def miniDea(A):
    [Sigma, Z, delta, z0, F] = A
    Z = getErreichbareZ(z0, Sigma, delta)
    A = [Sigma, Z, delta, z0, F]
    unterschZ = deaUnterscheidbareZustaende(A)
    
    for z in Z:
        if getZustandIndex(z, unterschZ) == -1:
            unterschZ.append(z)
    
    F_mini = set()
    for f in F:
        index = getZustandIndex(f, unterschZ)
        if index != -1:
            F_mini.add(unterschZ[index])
    
    delta_mini = {}
    for z in Z:
        for s in Sigma:
            index = getZustandIndex(z, unterschZ)
            index_to = getZustandIndex(list(delta[z,s])[0], unterschZ)
            delta_mini[unterschZ[index],s] = unterschZ[index_to]
    
    Z_mini = set(unterschZ)  # Neue Zustandsmenge
    
    A_mini = [Sigma, Z_mini, delta_mini, z0, F_mini]
    return A_mini

Sigma = {'a', 'b','c'}   
Z = {'Z5','Z6','Z7','Z8','Z4','Z1'}
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
delta1['Z1','a'] = set(['Z7'])
delta1['Z1','b'] = set(['Z6'])
delta1['Z1','c'] = set(['Z7'])
F = set(['Z4'])
A2 = [Sigma,Z,delta1,'Z4',F]
print(A2)
print(miniDea(A2))
