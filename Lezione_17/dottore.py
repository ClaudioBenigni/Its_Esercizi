from persona import Persona

class Doctor(Persona):
    def __init__(self, first_name, last_name, age, specialization, parcel):
        super().__init__(first_name, last_name, age)
        if not isinstance(specialization, str):
            raise ValueError("La specializzazione deve essere una stringa")
        if not isinstance(parcel, float):
            raise ValueError("La parcella deve essere un float")
        self._specialization = specialization
        self._parcel = parcel

    def getParcel(self):
        return self._parcel

    def getSpecialization(self):
        return self._specialization

    def isAValidDoctor(self):
        return self._age >= 30

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self._specialization}")