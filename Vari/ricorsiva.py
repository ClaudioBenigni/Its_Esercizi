def rimuovi(lista):
    print(lista)
    if len(lista) == 0:
        return
    print(lista[-1])
    rimuovi(lista[:-1])

rimuovi([10,20,30,40])