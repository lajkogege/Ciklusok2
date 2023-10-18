import math
def szamok(szam1:float, szam2:float):
    i:int=int(szam1)+1 #math.floor levágja a számrol a tízedest 
    while(i <= szam2):
        print(i, end=',')
        i+=1

