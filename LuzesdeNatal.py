t = int(input())
		
for  i in range (0,t):

    n = int(input())
    
    bina = str(format(n,"b"))
        
    for j in range(0,len(bina)):
        
        if bina[j]=='1':
            ver = True
            break
        
        
    if ver==True:
        cont=1
        maior=1
            
        for j in range(0,len(bina)):
            if bina[j]=='1' and bina[j-1]=='1':
                cont+=1
                if cont>maior:
                    maior=cont
                else:
                    cont=1
                
            
        print(maior)
        
    else :
        print("0")
            