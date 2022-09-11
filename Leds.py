# -*- coding: utf-8 -*-

n = int(input())

for i in range(0,n):
    led=0
    num = str(input())
    
    for j in num:
        if j=='0' or j=='6' or j=='9':
            led += 6
        elif j=='1':
            led += 2
        elif j=='2' or j=='3' or j=='5':
            led += 5
        elif j=='4':
            led += 4
        elif j=='7':
            led += 3
        elif j=='8':
            led += 7
    
    print(f"{led} leds")