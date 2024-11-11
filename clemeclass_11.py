class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    def aggiungi_ingrediente(self, ingrediente):
        self.ingredienti.append(ingrediente)

    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"

class Primo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def __str__(self):
        return f"Primo: {super().__str__()} - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"

class Secondo(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def __str__(self):
        return f"Secondo: {super().__str__()} - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"

class Dolce(Ricetta):
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, zucchero, tipo_dolce):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.zucchero = zucchero
        self.tipo_dolce = tipo_dolce

    def __str__(self):
        return f"Dolce: {super().__str__()} - Zucchero: {self.zucchero}g - Tipo Dolce: {self.tipo_dolce}"

def calcola_tempo_totale(ricette):
    return sum(ricetta.tempo_preparazione for ricetta in ricette)

def verifica_ingredienti(ricette, ingredienti_disponibili):
    ricette_possibili = []
    for ricetta in ricette:
        if all(ingrediente in ingredienti_disponibili for ingrediente in ricetta.ingredienti):
            ricette_possibili.append(ricetta)
    return ricette_possibili

def stampa_ricette(ricette):
    for ricetta in ricette:
        print(ricetta)

# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ingredienti_disponibili = ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"]
ricette_possibili = verifica_ingredienti(ricette, ingredienti_disponibili)

print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")
print("\nInformazioni sulle ricette:")
stampa_ricette(ricette_possibili)