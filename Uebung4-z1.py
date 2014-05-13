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
        m = primRek(n,k,m)
    return m