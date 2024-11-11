# Definizione della classe Auto
class Auto:
    # Costruttore della classe Auto
    def __init__(self, marca, modelo):
        # Inizializzazione degli attributi della classe Auto
        self.marca = marca  # marca dell'auto
        self.modello = modelo  # modello dell'auto
        self.motore = None  # motore associato all'auto (inizialmente None)

    # Metodo per associare un motore all'auto
    def associa_motore(self, motore):
        # Assegna il motore passato come argomento all'attributo motore dell'auto
        self.motore = motore


# Definizione della classe Motore
class Motore:
    # Costruttore della classe Motore
    def __init__(self, numero_seriale, tipo):
        # Inizializzazione degli attributi della classe Motore
        self.numero_seriale = numero_seriale  # numero seriale del motore
        self.tipo = tipo  # tipo del motore
        self.auto = None  # auto associata al motore (inizialmente None)

    # Metodo per associare un'auto al motore
    def associa_auto(self, auto):
        # Assegna l'auto passata come argomento all'attributo auto del motore
        self.auto = auto


# Creazione di un'istanza della classe Auto
auto1 = Auto("Fiat", "500")

# Creazione di un'istanza della classe Motore
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)  # associa il motore1 all'auto1
motore1.associa_auto(auto1)  # associa l'auto1 al motore1

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")  # stampa la marca e il modello dell'auto e il numero seriale del motore associato
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")  # stampa il numero seriale del motore e la marca e il modello dell'auto associata