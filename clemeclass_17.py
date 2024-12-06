class Insegnante:
    def __init__(self, nome, cognome, strumento):
        self.nome = nome
        self.cognome = cognome
        self.strumento = strumento
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def __str__(self):
        return f"Insegnante: {self.nome} {self.cognome}, Strumento: {self.strumento}"


class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.insegnante = None
        self.corsi = []

    def set_insegnante(self, insegnante):
        self.insegnante = insegnante
        insegnante.aggiungi_studente(self)

    def iscrivi_corso(self, corso):
        self.corsi.append(corso)
        corso.aggiungi_studente(self)

    def __str__(self):
        corsi = ', '.join([corso.nome for corso in self.corsi])
        return f"Studente: {self.nome} {self.cognome}, Insegnante: {self.insegnante.nome} {self.insegnante.cognome}, Corsi: {corsi}"


class Corso:
    def __init__(self, nome, durata):
        self.nome = nome
        self.durata = durata
        self.studenti = []

    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def __str__(self):
        return f"Corso: {self.nome}, Durata: {self.durata}"


def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(studente1)
    print(studente2)


if __name__ == "__main__":
    main()
