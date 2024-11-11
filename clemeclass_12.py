class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modello = modelo
        self.motore = None

    def associa_motore(self, motore):
        self.motore = motore


class Motore:
    def __init__(self, numero_seriale, tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None

    def associa_auto(self, auto):
        self.auto = auto
        
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)
motore1.associa_auto(auto1)

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")
