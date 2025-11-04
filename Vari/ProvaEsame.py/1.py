from string import punctuation
def lista_stringa (lista:list[str]) -> dict[str,int]:

    dizionario = {}
    lista_singole_stringhe = []

    for i in range(len(lista)):
        lista[i] = lista[i].lower()
        for p in punctuation:
            lista[i] = lista[i].replace(p, "")
    for i in lista:
        lista_singole_stringhe += i.split()
    
    for i in lista_singole_stringhe:
        if i in dizionario:
            dizionario[i] += 1
        else:
            dizionario[i] = 1

    return dizionario

print(lista_stringa(["ciao", "ciao, come, stai?"]))