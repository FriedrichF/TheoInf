'''
Created on 06.05.2014

@author: Friedrich
'''
def read(u,v,a): # liefert den Inhalt von Ra
  var = 'test'
  print(var)
  i = 0
  while (i < len(u) and u[i] != a): # Index a suchen
    i = i + 1
  if (i == len(u)): # Listen erweitern
    u += [a]
    v += [0]
  return v[i] # Inhalt von Ra zurueck
  
def write(u,v,a,b): # schreibt b in Ra
  i = 0
  while (i < len(u) and u[i] != a): # Index a suchen
    i = i + 1
  if (i == len(u)): # Listen erweitern
    u += [a]
    v += [0]
  v[i] = b # schreibt b in Ra
  
def main():
  var = 'TEST'
  print(var)
  br = 0
  u = [0, 1, 2, 3]    # Liste der Indizes 
  v = [0, 1, 2, 3]    # Liste mit entsp. Inhalt
  while (br < 7):      # Endebedingung STOP erreicht
    if (br == 0):
      i = read(u,v,2)
      j = read(u,v,i)
      write(u,v,3,j)
      br = br + 1
    if (br == 1):
      i = read(u,v,3) + read(u,v,2)
      write(u,v,3,i)
      br = br + 1
    if (br == 2):
      i = read(u,v,2) + read(u,v,1)
      write(u,v,2,i)
      br = br + 1
    if (br == 3):
      i = read(u,v,3)
      j = read(u,v,2)
      write(u,v,j,i)
      br = br + 1
    if (br == 4):
      i = read(u,v,0) - read(u,v,1)
      if (i < 0):
        i = 0
      write(u,v,0,i)
      br = br + 1
    if (br == 5):
      if (read(u,v,0) > 0):
        br = 0
      else:
        br = br + 1
    if (br == 6):
      i = read(u,v,2)
      j = read(u,v,i)
      write(u,v,0,j)
      br = br + 1
  print(read(u,v,0))
  return -1
  
main()