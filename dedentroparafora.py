# -*- coding: utf-8 -*-

n = int(input())

for i in range(0,n):
    frase = str(input())
    n = len(frase)
    n1 = (n//2)-1
    n2 = n-1
    n3 = n//n2
    
    for j in range(n1,-1,-1):
        print(frase[j], end="")
    for k in range(n2,n1,-1):
        print(frase[k], end="")
    print()