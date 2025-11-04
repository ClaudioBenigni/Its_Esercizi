classi={"classe1":["Marco", "Anna", "Giulia"],"classe2":["Luca", "Sara"]}

classi["classe2"].append("Paolo")

print(classi["classe2"])

parole = ["sole", "mare", "sole", "vento", "mare", "sole"]

dict1={}  
for i in parole:    
    if i not in dict1.keys():
        dict1[i]=1
    
    else:
        dict1[i]+=1 

print(dict1)


prezzi = {"mela": 1.2, "banana": 0.8, "pera": 1.5}

somma=0
for chiave,valore in prezzi.items():
    somma+=valore
print(somma)
print(sum(prezzi.values()))

temperature = {"Lun": 18, "Mar": 21, "Mer": 20, "Gio": 23, "Ven": 19}
print(max(temperature.values()))
    
rubrica = {"Luca": 3451234567, "Anna": 3287654321, "Paolo": 3499876543, "Giulia": 3201122334}

dict2={} 
lista1 = []
for chiave, valore in rubrica.items():
    if chiave[0] == "A" or chiave[0] == "G":
        lista1.append(chiave)
        dict2[chiave]=valore

print(dict2) 
