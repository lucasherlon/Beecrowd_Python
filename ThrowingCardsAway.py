
while True:
    n = int(input())
    if n==0:
        break
    
    fila = []
    filad=[]
    for i in range(0,n):
        fila.append(i+1)
        
    while len(fila)>1:
        filad.append(fila[0])
        del fila[0]
        if len(fila)==1:
            break
        fila.append(fila[0])
        del fila[0]
       
    
    print("Discarded cars: ", end="")
    for i in range(0,n-1):
        if(i!=n-2):
            print(f"{filad[i]}, ", end="")
        else:
            print(f"{filad[i]}")
    print(f"Remaining card: {fila[0]}")
        