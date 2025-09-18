from persona import Persona

class Paziente(Persona):
    
    def __init__(self, first_name, last_name, age,IDcode):
        super().__init__(first_name=first_name,last_name=last_name,age=age)
        self._IDcode=IDcode
    
    def setidCode(self,IDcode):
        if not isinstance(IDcode,str):
            raise ValueError("Il codice deve essere una stringa")
        
        else:
            self._IDcode=IDcode

    def getidCode(self):
        return self._IDcode
    
    def patientinfo(self):
        print(f"Il paziente {self._first_name} {self._last_name} ha il codice indentificativo:{self._IDcode}")