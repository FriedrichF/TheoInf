0 IF R0>0 GOTO 3  //Prüfen ob a 0 ist
1 IF R1>0 GOTO 3  //Prüfen ob b 0 ist
2 GOTO 11   //Wenn a und b Null sind
3 IF R1=0 GOTO 10   //Schleife beginnen
4 R3<-R0-R1   
5 IF R3=0 GOTO 8  //Prüfen ob a größer b ist
6 R0<-R0 - R1  //Wenn ja b von a abziehen und in a speichern
7 GOTO 3   // nächsten möglichen Schleifendurchlauf starten
8 R1<-R1-R0   //Wenn b größer ist wird a von b abgezogen und in b gespeichert
9 GOTO 3   // nächsten möglichen Schleifendurchlauf starten
10 R2<-R0   //a zurückgeben
11 STOP      // Programmende