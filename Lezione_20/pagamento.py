class Pagamento:
    def __init__(self):
        self._importo_pagamento = 0.0

    def setPagamento(self, importo: float):
        self._importo_pagamento = importo

    def getPagamento(self) -> float:
        return self._importo_pagamento

    def dettagliPagamento(self) -> str:
        return f"Importo del pagamento: €{self._importo_pagamento:.2f}"

class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        return f"Importo del pagamento: €{self._importo_pagamento:.2f}, Contanti"

    def inPezziDa(self):
        self.pezzi = []
        restante = round(self._importo_pagamento, 2)

        while round(restante,2) > 0.001:  
            if restante >= 500:
                self.pezzi.append(500)
                restante -= 500
            elif restante >= 200:
                self.pezzi.append(200)
                restante -= 200
            elif restante >= 100:
                self.pezzi.append(100)
                restante -= 100
            elif restante >= 50:
                self.pezzi.append(50)
                restante -= 50
            elif restante >= 20:
                self.pezzi.append(20)
                restante -= 20
            elif restante >= 10:
                self.pezzi.append(10)
                restante -= 10
            elif restante >= 5:
                self.pezzi.append(5)
                restante -= 5
            elif restante >= 2:
                self.pezzi.append(2)
                restante -= 2
            elif restante >= 1:
                self.pezzi.append(1)
                restante -= 1
            elif restante >= 0.5:
                self.pezzi.append(0.5)
                restante -= 0.5
            elif restante >= 0.2:
                self.pezzi.append(0.2)
                restante -= 0.2
            elif restante >= 0.1:
                self.pezzi.append(0.1)
                restante -= 0.1

            restante = round(restante,2)  

        return self.pezzi

    def stampaPezzi(self):
        pezzi = self.inPezziDa()

        conteggio = {}
        for pezzo in pezzi:
            if pezzo in conteggio:
                conteggio[pezzo] += 1
            else:
                conteggio[pezzo] = 1
        
        risultato = []
        for taglio in sorted(conteggio.keys(), reverse=True):
            quantita = conteggio[taglio]
            if taglio >= 5:
                risultato.append(f"{quantita} banconota/e da €{taglio}")
            else:
                risultato.append(f"{quantita} moneta/e da €{taglio}")
        
        return "\n".join(risultato)


class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare: str, numero_carta: str, scadenza: str):
        super().__init__()
        self.nome_titolare = nome_titolare
        self.numero_carta = numero_carta
        self.scadenza = scadenza

    def dettagliPagamento(self):
        return (f"Importo del pagamento: €{self._importo_pagamento:.2f}, "
                f"Nome titolare: {self.nome_titolare}, "
                f"Carta: {self.numero_carta}, "
                f"Scadenza: {self.scadenza}")

if __name__ == "__main__":
    # Pagamenti in contanti
    c1 = PagamentoContanti()
    c1.setPagamento(150)
    c2 = PagamentoContanti()
    c2.setPagamento(95.25)

    # Pagamenti con carta di credito
    cc1 = PagamentoCartaDiCredito("Mario Rossi", "1234567890123456", "12/24")
    cc1.setPagamento(200)
    cc2 = PagamentoCartaDiCredito("Luigi Bianchi", "6543210987654321", "01/25")
    cc2.setPagamento(500)

    # Stampa
    print(c1.dettagliPagamento())
    print(f"{c1.getPagamento():.2f} euro da pagare in contanti con:")
    print(c1.stampaPezzi())
    print()

    print(c2.dettagliPagamento())
    print(f"{c2.getPagamento():.2f} euro da pagare in contanti con:")
    print(c2.stampaPezzi())
    print()

    print(cc1.dettagliPagamento())
    print()
    print(cc2.dettagliPagamento())