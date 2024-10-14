class Piatto:
    def __init__(self, nome, prezzo, disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = disponibile

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

    def get_prezzo(self):
        return self.prezzo


class Antipasto(Piatto):
    def __init__(self, nome, prezzo, ingredienti, porzione):
        super().__init__(nome, prezzo, True)  
        self.ingredienti = ingredienti
        self.porzione = porzione

    def __str__(self):
        return f"Antipasto: {self.nome} - {self.prezzo}€ - Disponibile - Ingredienti: {', '.join(self.ingredienti)} - Porzione: {self.porzione}"


class Primo(Piatto):
    def __init__(self, nome, prezzo, tipo_pasta, sugo):
        super().__init__(nome, prezzo, True)  
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def __str__(self):
        return f"Primo: {self.nome} - {self.prezzo}€ - Disponibile - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"


class Secondo(Piatto):
    def __init__(self, nome, prezzo, tipo_carne, cottura):
        super().__init__(nome, prezzo, True)  
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def __str__(self):
        return f"Secondo: {self.nome} - {self.prezzo}€ - Disponibile - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"


class Dolce(Piatto):
    def __init__(self, nome, prezzo, tipo_dolce, calorie):
        super().__init__(nome, prezzo, True)  
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie

    def __str__(self):
        return f"Dolce: {self.nome} - {self.prezzo}€ - Disponibile - Tipo Dolce: {self.tipo_dolce} - Calorie: {self.calorie}"


def calcola_conto(piatti):
    return sum(piatto.get_prezzo() for piatto in piatti)


def stampa_menu(piatti):
    for piatto in piatti:
        print(piatto)

antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)
