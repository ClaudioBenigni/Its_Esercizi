from enum import*

class Genere(StrEnum):
    uomo=auto()
    donna=auto()

class Voto:
    v:int

    def __init__(self,v:int):
        if v < 18 or v > 31:
            raise ValueError(f"Il voto deve essere tra 18 e 30")
        self.v=v
        

if __name__ == "__main__":
    print(Genere.uomo)
    print(Genere.donna)