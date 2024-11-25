class Studente:
    def __init__(self, nome, matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []  # Lista dei corsi a cui lo studente è iscritto
    
    def aggiungi_corso(self, corso):
        # Associa un corso allo studente, se non è già presente
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)  # Aggiungi lo studente al corso
    
    def lista_corsi(self):
        # Restituisce i titoli dei corsi
        return [corso.titolo for corso in self.corsi]
    

class Corso:
    def __init__(self, titolo, codice):
        self.titolo = titolo
        self.codice = codice
        self.studenti = []  # Lista degli studenti iscritti al corso
    
    def aggiungi_studente(self, studente):
        # Associa uno studente al corso, se non è già presente
        if studente not in self.studenti:
            self.studenti.append(studente)
    
    def lista_studenti(self):
        # Restituisce i nomi degli studenti
        return [studente.nome for studente in self.studenti]

# Creazione delle istanze di Studente
studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

# Creazione delle istanze di Corso
corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
    print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
    print(f"- {studente.nome} ({studente.matricola})")
