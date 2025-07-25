def cifra_xor(stringa, chiave):
    # Restituisce una lista dei valori ASCII cifrati con XOR
    lista_cifrata = []
    for x in stringa:
        lista_cifrata.append(ord(x) ^ chiave)
    return lista_cifrata

def decifra_xor(lista_cifrata, chiave):
    # Ricostruisce la stringa originale riapplicando lo XOR
    stringa = ""
    for numero in lista_cifrata:
        stringa += chr(numero ^ chiave)
    return stringa

# Lettura input da utente
testo = input("Inserisci la stringa da cifrare: ")
chiave = int(input("Inserisci il valore segreto: "))

# Cifratura
lista = cifra_xor(testo, chiave)
print("\nLista cifrata (valori XOR):")
print(lista)

# Decifratura
testo_decifrato = decifra_xor(lista, chiave)
print("\nStringa decifrata:")
print(testo_decifrato)
