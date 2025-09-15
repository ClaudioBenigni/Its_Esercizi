import sys
import random

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file name>")
    sys.exit(1)  # Uscita se manca l'argomento

# Legge l'intero file in modalità binaria
data = None
with open(sys.argv[1], "rb") as f:
    data = f.read()

# Sceglie una posizione casuale nel file
pos = random.randint(0, len(data) - 1)

# Sceglie un bit casuale da modificare (da 0 a 7)
bit = random.randint(0, 7)

# Legge il byte originale e modifica il bit selezionato
byte = data[pos]
byte = byte ^ (1 << bit)  # XOR per flip del bit

# Ricostruisce i dati con il byte modificato
data = data[:pos] + bytes([byte]) + data[pos + 1:]

# Scrive di nuovo nel file (modifica permanente)
with open(sys.argv[1], "wb") as f:
    f.write(data)

print(f"Modificato il bit {bit} al byte n. {pos} nel file '{sys.argv[1]}'")

