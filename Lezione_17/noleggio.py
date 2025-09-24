from film import Film

class Noleggio:
    def __init__(self, film_list: list):
        self.film_list = film_list
        self.rented_film = {}

    def isAvailable(self, film: Film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False

    def rentAMovie(self, film: Film, clientID: int):
        if self.isAvailable(film):
            self.film_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film: Film, clientID: int, days: int):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penalty = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penalty:.2f} euro!")
        else:
            print(f"Errore: il cliente {clientID} non ha noleggiato il film {film.getTitle()}!")

    def printMovies(self):
        print("Film disponibili in negozio:")
        for f in self.film_list:
            print(f"{f.getTitle()} - {f.getGenere()} -")

    def printRentMovies(self, clientID: int):
        if clientID in self.rented_film and self.rented_film[clientID]:
            print(f"Film noleggiati dal cliente {clientID}:")
            for f in self.rented_film[clientID]:
                print(f"{f.getTitle()} - {f.getGenere()} -")
        else:
            print(f"Il cliente {clientID} non ha film noleggiati.")
