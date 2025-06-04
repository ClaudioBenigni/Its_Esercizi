def filtra_e_aumenta_prezzi(prodotti):
    nuovi_prodotti = {}
    
    for nome in prodotti:
        prezzo = prodotti[nome]
        if prezzo < 50:
            prezzo_aumentato = prezzo * 1.10
            prezzo_arrotondato = round(prezzo_aumentato, 2)
            nuovi_prodotti[nome] = prezzo_arrotondato
            
    return nuovi_prodotti

lista = {"banana": 4, "diego": 51}

print(filtra_e_aumenta_prezzi(lista))
