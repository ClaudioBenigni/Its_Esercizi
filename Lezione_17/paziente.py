from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, age, IDcode):
        super().__init__(first_name, last_name, age)
        self._IDcode = IDcode

    def setIdCode(self, IDcode):
        if not isinstance(IDcode, str):
            raise ValueError("Il codice deve essere una stringa")
        self._IDcode = IDcode

    def getIdCode(self):
        return self._IDcode

    def patientInfo(self):
        print(f"Il paziente {self._first_name} {self._last_name} ha il codice identificativo: {self._IDcode}")
