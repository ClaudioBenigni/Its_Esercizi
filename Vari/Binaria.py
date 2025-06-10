def ricerca_binaria(lista, s):
    inizio = 0
    fine = len(lista) - 1

    while inizio <= fine:
        metà = (inizio + fine) // 2
        if lista[metà] == s:
            return True
        elif lista[metà] < s:
            inizio = metà + 1
        else:
            fine = metà - 1
    return False

lista = [2,3,4,23,56,57,134,124,242365]
print(ricerca_binaria(lista, 5))
print(ricerca_binaria(lista, 56))


