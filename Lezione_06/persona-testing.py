'''
from persona import Persona #Dal file persona.py importa la classe Persona

cb:Persona = Persona("Claudio","Benigni",19)

print(cb)
print(cb.name, cb.lastname, cb.age)

cb.displayData() #sfrutto displayData per visualizzare i dati relativi alla persona cb
'''

from persona2 import Persona #dal file persona2.py importo la classe Persona

cb:Persona = Persona()

cb.displayData()

cb.setName("Claudio")  #imposto il nome della persona cb
cb.displayData()

cb.setLastaname("Benigni") #imposto il cognome della persona cb
cb.setAge(19) #imposto l'età della persona cb
cb.displayData()

print(cb.getName(),cb.getLastname(),cb.getAge())