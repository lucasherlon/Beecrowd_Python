# -*- coding: utf-8 -*-

n1, g1 = str(input()).split(" ")

n = int(n1)
g = int(g1)

lista=[]

for i in range(0,n):
    runa = str(input()).split(" ")
    lista.append(runa)

dicio = dict(lista)

x = int(input())

listai= str(input()).split(" ")

soma =0

for i in listai:
    soma += int(dicio[i])

print(soma)
    
if soma>= g:
    print("You shall pass!")
else:
    print("My precioooous")