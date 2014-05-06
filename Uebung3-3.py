(z0,1)->(z0,1,R) //Z0: laufe bis zum ende nach rechts und setzte Trennzeichen 5
(z0,2)->(z0,2,R)
(z0,_)->(z6,5,L)
(z6,1)->(z6,1,L) //Z6: laufe bis zum ersten zeichen nach Links, dass noch nicht kopiert wurde
(z6,2)->(z6,2,L)
(z6,_)->(z2,_,R)
(z6,3)->(z2,3,R)
(z6,4)->(z2,4,R)
(z6,5)->(z6,5,L)
(z2,1)->(z3,3,R) //1 wird gespeichert und die 1 mit 3 ersetzt
(z2,2)->(z4,4,R) //2 wird gespeichert und die 2 mit 4 ersetzt
(z2,5)->(z7,5,L) 
(z7,4)->(z7,2,L) //z7: tausche die 3 und 4er zu 1er und 2er zurück
(z7,3)->(z7,1,L)
(z7,_)->(z8,_,R)
(z8,1)->(z8,1,R) //z8: laufe nach links, tausche trennzeichen aus und füge am ende +1 an
(z8,2)->(z8,2,R)
(z8,5)->(z8,_,R)
(z8,_)->(z1,1,O)
(z3,1)->(z3,1,R) //z3: die Gemerkte 1 wird am ende der Liste angefügt
(z3,2)->(z3,2,R)
(z3,5)->(z3,5,R)
(z3,_)->(z6,1,L)
(z4,1)->(z4,1,R) //z4: die Gemerkte 2 wird am ende der Liste angefügt
(z4,2)->(z4,2,R)
(z4,5)->(z4,5,R)
(z4,_)->(z6,2,L)