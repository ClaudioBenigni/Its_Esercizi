#Crea un dizionario persona con le chiavi:
#"nome" → "Luca"
#"età" → 25
#"città" → "Milano"
#Stampa:
#Il valore associato alla chiave "nome"
#Tutte le chiavi del dizionario
#Tutti i valori del dizionario

persona={"nome":"Luca","età":25,"città":"Milano"}

print(persona["nome"])
print(persona.keys())
print(persona.values())

persona["professione"]="ingegnere"
persona["età"]=26

print(persona)

persona.pop("città")
print(persona)

chiave=input("Quale chiave si vuole inserire?: ")
if chiave in persona.keys():
    print(f"{persona[chiave]}")

else:
    print("Chiave non trovata")