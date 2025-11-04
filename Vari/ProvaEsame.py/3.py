def sistema (lista:list[int])-> list:
    ordine=[]
    lista2=lista.copy()

    while lista2:
        minimo = lista2[0]
        for x in lista2:
            if x < minimo:
                minimo = x
        ordine.append(minimo)
        lista2.remove(minimo)

    return ordine

print(sistema([1,3,4,12,7]))