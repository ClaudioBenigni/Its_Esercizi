from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

if __name__ == "__main__":
    film_list = [
        Azione(1, "Die Hard"),
        Azione(2, "Mad Max"),
        Azione(3, "John Wick"),
        Azione(4, "The Dark Knight"),
        Azione(5, "Gladiator"),
        Commedia(6, "The Mask"),
        Commedia(7, "Mrs. Doubtfire"),
        Commedia(8, "Superbad"),
        Commedia(9, "The Hangover"),
        Drama(10, "The Shawshank Redemption")
    ]

    noleggio = Noleggio(film_list)

    print("Quale film vuoi noleggiare?\n")

    noleggio.rentAMovie(film_list[0], 101)
    noleggio.rentAMovie(film_list[1], 101)
    noleggio.rentAMovie(film_list[1], 202)
    noleggio.rentAMovie(film_list[5], 202)
    noleggio.giveBack(film_list[1], 101, 4)

    print("\nFilm disponibili in negozio dopo le operazioni:")
    noleggio.printMovies()
