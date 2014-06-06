'''
Friedrich Fell    Matnr.:2009756

Matthias Proestler    Matnr.:2016779

Uebungsgruppe 1
'''
def deaDefine():                    # definiert einen DEA A
    Sigma = {'a', 'b', 'c'}              # Alphabet
    Z = {'Z0','Za','Zac','Zacb','Zacba','Zacbac','Zacbaca','Zacbacac'}                   # Zustandsmenge
    delta = {}                      # Ueberfuehrungsfunktion
    delta['Z0','c'] = 'Z0'
    delta['Z0','b'] = 'Z0'
    delta['Zac','c'] = 'Z0'
    delta['Za','b'] = 'Z0'
    delta['Zacba','b'] = 'Z0'
    delta['Zacb','c'] = 'Z0'
    delta['Zacb','b'] = 'Z0'
    delta['Zacbac','c'] = 'Z0'
    delta['Zacbaca','b'] = 'Z0'
    delta['Za','a'] = 'Za'
    delta['Z0','a'] = 'Za'
    delta['Zac','a'] = 'Za'
    delta['Zacba','a'] = 'Za'
    delta['Zacbaca','a'] = 'Za'
    delta['Za','c'] = 'Zac'
    delta['Zac','b'] = 'Zacb'
    delta['Zacb','a'] = 'Zacba'
    delta['Zacba','c'] = 'Zacbac'
    delta['Zacbac','a'] = 'Zacbaca'
    delta['Zacbac','b'] = 'Zacb'
    delta['Zacbaca','c'] = 'Zacbacac'
    delta['Zacbacac','c'] = 'Zacbacac'
    delta['Zacbacac','b'] = 'Zacbacac'
    delta['Zacbacac','a'] = 'Zacbacac'
    F = {'Zacbacac'}                         # Menge der akzeptierenden Zustaende
    A = [Sigma, Z, delta, 'Z0', F]
    return A

def deaErweiterteUEF(delta, z, w):  # erweiterte Ueberfuehrungsfunktion eines DEA
    for a in w:
        z = delta[z, a]
    return z

def deaRun(A, w):                   # testet, ob der DEA A das Wort w akzeptiert
    [Sigma, Z, delta, z0, F] = A
    return deaErweiterteUEF(delta, z0, w) in F

A = deaDefine()
print(deaRun(A,'aaacbacbacac'))