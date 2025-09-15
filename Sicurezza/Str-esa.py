def stringa_a_esadecimale(stringa):
    """
    Converte una stringa in una rappresentazione esadecimale dei suoi byte UTF-8.
    Ritorna una stringa con i valori esadecimali separati da spazi.
    """
    esadecimale = stringa.encode('utf-8').hex()
    # Formattiamo in byte separati da spazi (2 caratteri per byte)
    esadecimale_formattato = ' '.join(esadecimale[i:i+2] for i in range(0, len(esadecimale), 2))
    return esadecimale_formattato

# Esempi di utilizzo
esempi = ["ciao", "Hello!", "😀", "123"]

for s in esempi:
    risultato = stringa_a_esadecimale(s)
    print(f"Stringa: '{s}' → Esadecimale: {risultato}")
