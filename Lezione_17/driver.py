from paziente import Paziente
from dottore import Doctor
from fattura import Fattura

if __name__ == "__main__":
    # Creazione pazienti
    p1 = Paziente("Luca", "Bianchi", 25, "PZ001")
    p2 = Paziente("Giulia", "Rossi", 30, "PZ002")
    p3 = Paziente("Marco", "Verdi", 40, "PZ003")
    p4 = Paziente("Anna", "Neri", 22, "PZ004")

    lista_pazienti1 = [p1, p2, p3]
    lista_pazienti2 = [p4]

    # Creazione dottori validi
    dottore_1 = Doctor("Paolo", "Ferrari", 45, "Cardiologo", 100.0)
    dottore_2 = Doctor("Chiara", "Russo", 38, "Neurologo", 120.0)

    # Presentazione dottori
    dottore_1.doctorGreet()
    dottore_2.doctorGreet()

    # Creazione fatture
    fattura1 = Fattura(lista_pazienti1, dottore_1, parcel=dottore_1.getParcel())
    fattura2 = Fattura(lista_pazienti2, dottore_2, parcel=dottore_2.getParcel())

    # Stampa salari iniziali
    print(f"Salario Dottore1: {fattura1.salary} euro!")
    print(f"Salario Dottore2: {fattura2.salary} euro!")

    # Spostamento paziente da dottore1 a dottore2
    fattura1.removePatient("PZ003")
    fattura2.addPatient(p3)

    # Stampa salari aggiornati
    print(f"Salario Dottore1: {fattura1.salary} euro!")
    print(f"Salario Dottore2: {fattura2.salary} euro!")

    # Guadagno totale ospedale
    guadagno_totale = fattura1.salary + fattura2.salary
    print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")