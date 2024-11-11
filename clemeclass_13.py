class Stanza:
    def __init__(self, nome, superficie):
        self.nome = nome
        self.superficie = superficie
    
    # Metodi getter
    def get_nome(self):
        return self.nome
    
    def get_superficie(self):
        return self.superficie
    
    # Metodi setter
    def set_nome(self, nome):
        self.nome = nome
    
    def set_superficie(self, superficie):
        self.superficie = superficie


class Casa:
    def __init__(self, indirizzo, proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []  # Lista per contenere le stanze della casa
    
    # Metodi getter
    def get_indirizzo(self):
        return self.indirizzo
    
    def get_proprietario(self):
        return self.proprietario
    
    def get_stanze(self):
        return self.stanze
    
    # Metodo setter
    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo
    
    def set_proprietario(self, proprietario):
        self.proprietario = proprietario
    
    # Metodo per aggiungere una stanza
    def aggiungi_stanza(self, stanza):
        self.stanze.append(stanza)


# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.get_proprietario()} situata in {casa.get_indirizzo()} contiene le seguenti stanze:")
for stanza in casa.get_stanze():
    print(f"- {stanza.get_nome()} ({stanza.get_superficie()} mq)")
