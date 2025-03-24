class Persona:
    
    def __init__(self):

        self.name = ""
        self.lastname = ""
        self.age = ""
    
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
    
    # funzione che consenste di dare un valore a self.name
    
    def setName(self, name:str) -> None:
        self.name = name
    
    # funzione che consente di impostare un valore a self.lastname

    def setLastaname(self, lastname:str) -> None:
        self.lastname = lastname
    # funzione che consente di impostare un valore a self.lastname

    def setAge(self, age:int) -> None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age = age
    
    # funzione che restituisce il valore di self.name

    def getName(self) -> str:
        return self.name
    
    # funzione che restituisce il valore di self.lastname

    def getLastname(self) -> str:
        return self.lastname
    
    # funzione che restituisce il valore di self.age

    def getAge(self) -> int:
        return self.age