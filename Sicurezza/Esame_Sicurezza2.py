#2-1
messaggio_cifrato = 204751668535
modulo = 514948966453
e = 3

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

found = False  # Quando diventa True vuol dire che la parole è stata trovata usato per fermare tutto

# Con i cicli annidati genero tutte le parole da 5 caratteri(52^5)
for p1 in alfabeto:
    # controllo il flag all'inizio di ogni ciclo esterno così da poterlo interrompere
    if found:
        break
    for p2 in alfabeto:
        if found:
            break
        for p3 in alfabeto:
            if found:
                break
            for p4 in alfabeto:
                if found:
                    break
                for p5 in alfabeto:
                    if found:
                        break

                    # Combino i cinque caratteri per ottenere la parola 
                    plain_text = p1 + p2 + p3 + p4 + p5

                    # Conversione stringa a intero
                    # plain_text.encode("utf-8").hex() prende la parola e la trasforma
                    # in esadecimale come stringa.
                    # int(..., 16) prende la stringa e la interpreta come numero.
                    # In pratica otteniamo l'intero corrispondente ASCII della parola.
                    plain_text_hex = plain_text.encode("utf-8").hex()
                    m = int(plain_text_hex, 16)
                    
                    # pow(m, e, modulo) calcola (m**e) % modulo in modo efficiente.
                    # Quindi qui stiamo "cifrando" m con e=3 e il modulo dato.
                    cifrato = pow(m, e, modulo)

                    # Se corrisponde, allora la parola è giusta.
                    if cifrato == messaggio_cifrato:
                        print(f"Parola trovata:{plain_text}")
                        print(f"M={m}")
                        found = True  # SEgna che abbiamo trovato la parola
                        break  # Esce dal ciclo 



#2-2
import math

C = 10002041662569686       
n = 51151902024533551      
e = 3                       
sqrt_n = int(math.isqrt(n)) # Radice quadrata di n

for i in range(sqrt_n, 1, -1):  # Provo i possibili divisori di n iniziando dai numeri più grandi fino a trovare p

    if n % i == 0:
        p = i   # Ho trovato un numero che divide n, lo chiamo p
        q = n // i  # L 'altro fattore q si ottiene dividendo n per p
        break

Eu = (p - 1) * (q - 1)  # Eulero (serve per la chiave privata)
d = pow(e, -1, Eu)  # Trovo d, la chiave privata, usando l'inverso modulo
CD_int = pow(C, d, n)   # Formula RSA: plaintext = C^d mod n

# Converto il numero in byte e poi in una parola leggibile
num_bytes = (CD_int.bit_length() + 7) // 8   # Calcolo quanti byte servono
plain_bytes = CD_int.to_bytes(num_bytes, 'big')  # Converto in byte
plain_text = plain_bytes.decode('utf-8')         # Converto i byte in testo

print(f"Messaggio cifrato:{C}")
print(f"Messaggio decifrato:{plain_text}")

