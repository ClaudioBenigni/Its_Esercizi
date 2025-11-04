studenti = {
    "s001": {"nome": "Anna", "età": 20, "corso": "Informatica"},
    "s002": {"nome": "Luca", "età": 22, "corso": "Matematica"},
    "s003": {"nome": "Sara", "età": 21, "corso": "Fisica"}
}

print(studenti["s002"]["nome"])
print(studenti.keys())
studenti["s004"]={"nome":"Domenico","età":20,"corso":"Cyber"}  
print(studenti)

studenti["s001"]["età"]=21
studenti["s003"]["corso"]="ingegneria"
print(studenti)     