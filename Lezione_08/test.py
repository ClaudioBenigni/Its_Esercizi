
from persona import Persona
from studente import Studente

p: Persona = Persona("Claudio", "Benigni", 19)
print(p)

studente1: Studente = Studente("Mario", "Rossi", 20, "0123456")
print("\n", studente1)

if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

if isinstance(studente1, Persona):
    print("studente1 è anche istanza della classe Persona")

if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")

if isinstance(p, Studente):
    print("p è un oggetto sia della classe Persona che Studente")
else:
    print("p è un oggetto della classe Persona ma non è un oggetto della classe Studente")

if issubclass(Studente, Persona):
    print("\nStudente è sottoclasse di Persona")
