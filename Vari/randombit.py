import sys
import random

if len(sys.argv) !=2:
    print(f"Usage:{sys.argv[0]} <file name>")
    
#devo leggere tutti i file
data=None
with open(sys.argv[1], "rb") as f:
    data = f.read()

#prendo un byte casuale dal file
pos = random.randit(0, len(data)-1)

#prendo un bit casuale del byte
bit = random.randit(0,7)

#ora devo cambiare il valore del bit
byte = data[pos]
byte = byte^(1<<bit) 

data = data[:pos] + bytes([byte]) + data[pos+1:]  

with open(sys.argv[1] "wb") as f:
    f.write(data)

print(f"Modificato il bit {bit} al posto {pos} nel file {sys.argv[1]}")    

