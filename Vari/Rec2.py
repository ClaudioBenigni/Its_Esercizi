def odd(lista):
    dizionario={"pos":[],"neg":[]}

    for numero in lista:
        if numero >=0:
            dizionario["pos"].append(numero)  
        else:
            dizionario["neg"].append(numero)  

    return dizionario

lista=[1,2,-7,5,-93,31,-3] 

print(odd(lista))