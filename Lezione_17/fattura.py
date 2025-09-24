from persona import Persona
from paziente import Paziente
from dottore import Doctor

class Fattura:
    def __init__(self, pazienti, dottore, parcel=100):
        if dottore.isAValidDoctor():
            self.dottore = dottore
            self.pazienti = pazienti
            self.parcel = parcel
            self.fatture = len(pazienti)
            self.salary = self.getSalary()
        else:
            self.dottore = None
            self.pazienti = None
            self.parcel = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getFatture(self):
        return len(self.pazienti) if self.pazienti else 0

    def getSalary(self):
        return len(self.pazienti) * self.parcel if self.pazienti else 0

    def addPatient(self, newPatient):
        if self.pazienti is not None:
            self.pazienti.append(newPatient)
            self.fatture = self.getFatture()
            self.salary = self.getSalary()
            print(f"Alla lista del Dottor {self.dottore.get_last_name()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else:
            print("Impossibile aggiungere pazienti: dottore non valido!")

    def removePatient(self, idCode):
        if self.pazienti is not None:
            for paziente in self.pazienti:
                if paziente.getIdCode() == idCode:
                    self.pazienti.remove(paziente)
                    self.fatture = self.getFatture()
                    self.salary = self.getSalary()
                    print(f"Alla lista del Dottor {self.dottore.get_last_name()} è stato rimosso il paziente {idCode}")
                    return
            print(f"Nessun paziente con codice {idCode} trovato nella lista del Dottor {self.dottore.get_last_name()}.")
        else:
            print("Impossibile rimuovere pazienti: dottore non valido!")