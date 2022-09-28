while True:
    try:
        n,m = str(input()).split()
        n = int(n)
        soma=0
        for i in m:
            soma = soma + int(i)
        
        if soma%3==0:
            print(f'{soma} sim')
        else:
            print(f'{soma} nao')
    
    except EOFError:
        break
        