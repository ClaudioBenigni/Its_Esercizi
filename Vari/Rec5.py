def moltiplica_minori_di_threshold(lista, threshold):
    risultato = 1
    for numero in lista:
        if numero % 1 == 0 and numero < threshold:
            risultato *= numero
    return risultato

lista = (1, 5, 6, 3, 7, 98, 2, 35413, 6543, 2, 14, 414, 6, 56)
tr = 10

print(moltiplica_minori_di_threshold(lista, tr))