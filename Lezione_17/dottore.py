from persona import Persona

class Doctor(Persona):

    def __init__(self, first_name, last_name, age,specialization,parcel):
        super().__init__(first_name=first_name,last_name=last_name,age=age)

        if not isinstance(specialization,str):
            raise ValueError("La specializzazione deve essere una stringa")
        
        if not isinstance(parcel,float):
            raise ValueError("La parcella deve essere un float")
    
        self._specialization=specialization
        self._parcel=parcel

    def setSpecialization(self,specialization):
        if not isinstance(specialization, str):
            raise ValueError("Errore: la specializzazione deve essere una stringa")
        self._specialization = specialization

    def setParcel(self, parcel):
        if not isinstance(parcel, float):
            raise ValueError("Errore: la parcella deve essere un numero float")
        self._parcel = parcel
    
    def getSpecialization(self):
        return self._specialization
    
    def getParcel(self):
        return self._parcel
    
    def isAValidDoctor(self):
        if self._age >= 30:
            print(f"Il dottore {self._first_name} {self._last_name} è un dottore valido")

        else:
            print(f"Il dottore {self._first_name} {self._last_name} non è un dottore valido")
    
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self._specialization}")