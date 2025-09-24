from film import Film

class Azione(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Azione"
        self._penale = 3.00
    
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, ritardo: int):
        return self._penale * ritardo


class Commedia(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Commedia"
        self._penale = 2.50
    
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, ritardo: int):
        return self._penale * ritardo


class Drama(Film):
    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Drama"
        self._penale = 2.00
    
    def getGenere(self):
        return self._genere
    
    def getPenale(self):
        return self._penale
    
    def calcolaPenaleRitardo(self, ritardo: int):
        return self._penale * ritardo
