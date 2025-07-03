from datetime import date
from typing import List


class Progetto:
    def __init__(self, nome: str, budget: float):
        self.nome = nome
        self.budget = budget
        self.impiegati_coinvolti: List['Impiegato'] = []

    def aggiungi_impiegato(self, impiegato: 'Impiegato'):
        self.impiegati_coinvolti.append(impiegato)
        impiegato.progetti.append(self)


class Dipartimento:
    def __init__(self, nome: str, telefoni: List[str], indirizzo: str):
        self.nome = nome
        self.telefoni = telefoni
        self.indirizzo = indirizzo
        self.impiegati: List['Impiegato'] = []
        self.progetti_diretti: List[Progetto] = []

    def aggiungi_impiegato(self, impiegato: 'Impiegato'):
        self.impiegati.append(impiegato)
        impiegato.dipartimento = self

    def aggiungi_progetto_diretto(self, progetto: Progetto):
        self.progetti_diretti.append(progetto)


class Impiegato:
    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: float, dipartimento: Dipartimento):
        self.nome = nome
        self.cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio
        self.dipartimento = dipartimento
        self.progetti: List[Progetto] = []
        dipartimento.aggiungi_impiegato(self)
