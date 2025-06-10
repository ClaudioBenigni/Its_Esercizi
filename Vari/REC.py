def esercizio_2(lista: list[int|float]) -> dict[str, list[int|float]]:
    
    dizionario_1: dict[str, list[int|float]] = {"positivi": [], "negativi": []}
    
    for element in lista:
        
        if element >= 0:
            
            dizionario_1["positivi"].append(element)
            
        else:
            
            dizionario_1["negativi"].append(element)
            
    return dizionario_1




lista: list[int|float] = [1, 2, -4, 5, -7, 42, 78, -94]

risultato: dict[str, list[int|float]] = esercizio_2(lista=lista)
print(risultato)


prodotti: dict[str, float] = {"Samsung A55": 280.0, "Pennarello": 1.5}

def esercizio_3(prodotti: dict[str, float]) -> dict[str, float]:
    
    dizionario: dict[str, float] = {}
    
    for key, value in prodotti.items():
        
        if value < 50:
            
            dizionario[key] = round(value * 1.10, 2)
            
    return dizionario


risultato: dict[str, float] = esercizio_3(prodotti=prodotti)

print(risultato)

        
def nome_funzione(lista: list[int]) -> int:
    
    pass





class Movie:
    
    def __init__(self, movie_id: str, title: str, director: str):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
        
        
    def rent(self) -> None:
        
        if self.is_rented:
            
            print("Errore: il film è gia stato noleggiato!")
            
        else:
            
            self.is_rented = True
            
    def return_movie(self) -> None:
        
        if not self.is_rented:
            
            print("Errore: il film non è stato affittato a nessuno!")
            
        else:
            
            self.is_rented = False
            
            
class Customer:
    
    def __init__(self, customer_id: str, name: str):
        
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []
        
    def rent_movie(self, movie: Movie) -> None:
        
        if movie.is_rented:
            
            print("Errore: il film è gia stato affittato a qualcuno!")
            
        else:
            
            movie.rent()
            self.rented_movies.append(movie)
            
            
    def return_movie(self, movie: Movie) -> None:
        
        if movie in self.rented_movies:
            
            
            movie.return_movie()
            self.rented_movies.remove(movie)
            
        else:
            
            print("Errore: il cliente non ha noleggiato questo film!")
            
    
class VideoRentalStore:
    
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        
        self.movies = movies
        self.customers = customers
        
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        
        if movie_id not in self.movies:
            
            movie: Movie = Movie(movie_id, title, director)
            
            # self.movies[movie_id] = movie
            
            tupla: tuple = (movie_id, movie)
            
            self.movies.update(tupla)
            
        else:
            
            print("Il film è già all'interno del catalogo!")
            
        
        
    def register_customer(self, customer_id: str, name: str) -> None:
        
        if customer_id not in self.customers:
            
            customer: Customer = Customer(customer_id, name)
            
            self.customers[customer_id] = customer
            
        else:
            
            print("Il cliente è già presente nell'anagrafica!")
    
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            
            movie: Movie = self.movies[movie_id]
            
            self.customers[customer_id].rent_movie(movie) 
            
        else:
            
            print("Cliente o film non trovato!")
            
    def return_movie(self, customer_id: str, movie_id: str) -> None:
        
        if movie_id in self.movies and customer_id in self.customers:
            
            movie: Movie = self.movies[movie_id]
            
            self.customers[customer_id].return_movie(movie) 
            
        else:
            
            print("Cliente o film non trovato!")
            
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        
        if customer_id in self.customers:
            
            return self.customers[customer_id].rented_movies
        
        else:
            
            print("Il cliente non esiste!")
    
    def get_all_movies(self) -> list[Movie]:
        """
        la funzione deve restituire la lista di tutti i film affittati da ogni cliente
        del videonoleggio
        """
        
        film_noleggiati: list[Movie] = []
        
        for _, customer in self.customers.items():
            
            film_noleggiati += customer.rented_movies
        
        return film_noleggiati