# -*- coding: utf-8 -*-

n = int(input())
soma=0.0
somap=0.0
lista=[]
for i in range(0,n):
    preco = float(input())
    prod = str(input()).split()
    lista.append(len(prod))
    soma += len(prod)
    somap += preco
    prod=[]
    preco =0

for i in range(0,n):
    print(f'day {i+1}: {lista[i]} kg')

print(f'{soma/n:.2f} kg by day')
print(f'R$ {somap/n:.2f} by day')