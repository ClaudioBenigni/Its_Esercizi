# Primo modulo RSA (n)
n = int(
    "00d3bde010ebe6fe526c956aa3a3f0"
    "5a92b95aa63aaf9c39e174eb02f4d3"
    "3722b6f878f2b81341d69f2245f2d5"
    "73962842412a4aa4e4284ea5d4c080"
    "1f5d950a2ddb6402e650b756171528"
    "7b7275d4751023a1c430c491cbb21f"
    "4a26ebb5eecd643b5d67ae5630f9e1"
    "8518e1bb4101ea72c469736f6b5eb0"
    "40cdc99482c47b98a5c0d7b64e5bc9"
    "3c91b604e9115870c67eedaa1fa618"
    "5b0e45a52483faaa2edb58665c6165"
    "0dfe61b4b0eba3ca7f770d3d8e487b"
    "accc220058e32895e24d3bfd388329"
    "b57a1a657252b2918f758b172f4e1b"
    "3c3ea43d3e62d75856b03387cbba35"
    "766db2fd625844fcdb38f62d1c1a4c"
    "c176c926338f65487e014711302aac"
    "10ad", 16
)

# Esponente pubblico
e = 3

# Messaggio originale
msg = "Ciao,come va...?"
msg_int = int(msg.encode("utf-8").hex(), 16)

# Prima cifratura RSA
C1 = pow(msg_int, e, n)
print("C1:", C1)

# Secondo modulo RSA (n2)
n2 = int(
    "234a5002d1fbd50dbcc391c5f0a80f"
    "187439c65f1d44b4503e272b28cdde"
    "85c929697dc9588af91a85b6532393"
    "43b1606031b71b7b5c0d1ba3756aaf"
    "e4ee2c5cf9e6007bb81e8e592e3169"
    "e868f8be2d5b45a0b2cb6da1f30537"
    "067c9e527790b48f9147b90829a596"
    "2ed049e02afc687611933d3c8fc80a"
    "ccf6ee15cb69eec5fce357ed36020a"
    "16d1ad18e346a666fa47d0fbfbdf0d"
    "19faba30ee4fd0b25920dcca9cc0af"
    "944419f630efd25823775e3bc1bfae"
    "24e05be58562d23139da3b91ac8bc6"
    "e7a83ab52d1c564f1e624ef1acb48c"
    "71358684dee15a95ae805a7170bb3a"
    "6e43df4430dd0de59eaea53391a903"
    "6b189c633cc635b920341b127a4955"
    "fb", 16
)

# Seconda cifratura (sul risultato della prima)
# Qui non serve nessuna encode: C1 è già un numero
C2 = pow(C1, e, n2)
print("C2:", C2)
