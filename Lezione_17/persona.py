class Persona:
    def __init__(self, first_name, last_name, age):
        if not isinstance(first_name, str):
            raise ValueError("Errore: il nome deve essere una stringa")
        if not isinstance(last_name, str):
            raise ValueError("Errore: il cognome deve essere una stringa")
        if not isinstance(age, int):
            raise ValueError("Errore: l'età deve essere un numero intero")

        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def set_first_name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError("Errore: il nome deve essere una stringa")
        self._first_name = first_name

    def set_last_name(self, last_name):
        if not isinstance(last_name, str):
            raise ValueError("Errore: il cognome deve essere una stringa")
        self._last_name = last_name

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Errore: l'età deve essere un numero intero")
        self._age = age

    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    def get_age(self):
        return self._age
    
    def greet(self):
        print(f"Ciao {self._first_name} {self._last_name}, hai {self._age} anni")
