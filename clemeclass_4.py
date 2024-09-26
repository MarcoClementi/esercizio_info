class Calcolatrice:
    @staticmethod
    def addizione(numero1, numero2):
        return numero1 + numero2

    @staticmethod
    def sottrazione(numero1, numero2):
        return numero1 - numero2

    @staticmethod
    def moltiplicazione(numero1, numero2):
        return numero1 * numero2

    @staticmethod
    def divisione(numero1, numero2):
        if numero2 == 0:
            raise ValueError("Impossibile dividere per 0")
        return numero1 / numero2

# Esempio di utilizzo
print(Calcolatrice.addizione(10, 5))       # Output: 15
print(Calcolatrice.sottrazione(10, 5))     # Output: 5
print(Calcolatrice.moltiplicazione(10, 5)) # Output: 50
print(Calcolatrice.divisione(10, 5))       # Output: 2.0