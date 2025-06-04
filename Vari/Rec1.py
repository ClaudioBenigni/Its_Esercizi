lista_tuple=[(1,"a"),(2,"b"),(3,"c")]  

def convert(lista):
    dizionario={}
    for elemento in lista:
        chiave,valore = elemento[0], elemento[1]  
        if chiave in dizionario:
            dizionario[chiave] += valore
        else:
            dizionario[chiave] = valore

    return dizionario   

print(convert(lista_tuple))