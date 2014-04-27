def divtwo(x):
    d = 0
    if (x <= 0):
        d = 0
    if (x > 0):
        while (x >= 2):
            d = (d + 1)
            x = (x - 2)
    return d
            
def decToBin(n):
    if (n <= 0):
        print(0)
    while (n > 0):
        gesamt = 0
        div = divtwo(n)
        for i in range(0, div):
            gesamt = gesamt + 2
        print (n - gesamt)
        n = div
    
decToBin(6)