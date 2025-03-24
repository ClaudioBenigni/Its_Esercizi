class Persona:

    def __init__(self,name:str,lastname:str,age:int):
    
        self.name = name
        self.lastname = lastname
        self.age = age
    
    #Funzione della classe che visualizza in output i dati di una persona

    def displayData(self) -> None:
        print(f"Nome{self.name}\nCognome {self.lastname}\nEtà {self.age}")