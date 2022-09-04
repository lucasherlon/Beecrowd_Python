while True:
    try:
        n = str(input()).split(":")
        
        hr = int(n[0])
        minut = int(n[1])
        
        if hr<7:
            print("Atraso maximo: 0")
        elif hr<8:
            atraso = minut
            print(f"Atraso maximo: {atraso}")
        elif hr==9:
            atraso=120
            print(f"Atraso maximo: {atraso}")
        else:
            hr += 1
            atraso = ((hr-int(n[0])) * 60) + minut
            print(f"Atraso maximo: {atraso}")
    
    except EOFError:
        break
