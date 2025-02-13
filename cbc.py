from datetime import date
from typing import List, Optional

class Libro:
    def __init__(self, titolo: str, data_pubblicazione: date, autore: "Autore"):
        self.titolo = titolo
        self.data_pubblicazione = data_pubblicazione
        self.data_prestito: Optional[date] = None
        self.data_restituzione: Optional[date] = None
        self.utente_corrente: Optional["Utente"] = None
        self.autore = autore

    def disponibile(self) -> bool:
        """Verifica se il libro è disponibile per il prestito"""
        return self.utente_corrente is None

    def __str__(self):
        return f"{self.titolo} ({self.data_pubblicazione.year}) - {self.autore.nome} {self.autore.cognome}"


class Autore:
    def __init__(self, nome: str, cognome: str):
        self.nome = nome
        self.cognome = cognome
        self.libri: List[Libro] = []

    def aggiungi_libro(self, libro: Libro):
        """Aggiunge un libro alla lista di libri scritti dall'autore"""
        self.libri.append(libro)

    def ottieni_libri(self) -> List[Libro]:
        """Restituisce la lista di libri scritti dall'autore"""
        return self.libri

    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Utente:
    def __init__(self, nome: str, cognome: str):
        self.nome = nome
        self.cognome = cognome
        self.libri_in_prestito: List[Libro] = []

    def ottieni_libri_in_prestito(self) -> List[Libro]:
        """Restituisce la lista di libri attualmente in prestito all'utente"""
        return self.libri_in_prestito

    def __str__(self):
        return f"{self.nome} {self.cognome}"


class Biblioteca:
    def __init__(self):
        self.libri: List[Libro] = []
        self.utenti: List[Utente] = []

    def aggiungi_libro(self, libro: Libro):
        """Aggiunge un libro alla biblioteca"""
        self.libri.append(libro)

    def aggiungi_utente(self, utente: Utente):
        """Aggiunge un utente alla biblioteca"""
        self.utenti.append(utente)

    def ottieni_libri(self) -> List[Libro]:
        """Restituisce tutti i libri presenti in biblioteca"""
        return self.libri

    def ottieni_utenti(self) -> List[Utente]:
        """Restituisce tutti gli utenti registrati in biblioteca"""
        return self.utenti

    def presta_libro(self, libro: Libro, utente: Utente, data_prestito: date) -> bool:
        """Assegna un libro a un utente se disponibile"""
        if libro.disponibile():
            libro.utente_corrente = utente
            libro.data_prestito = data_prestito
            utente.libri_in_prestito.append(libro)
            return True
        return False

    def restituisci_libro(self, libro: Libro, data_restituzione: date) -> bool:
        """Permette a un utente di restituire un libro"""
        if libro.utente_corrente:
            libro.utente_corrente.libri_in_prestito.remove(libro)
            libro.utente_corrente = None
            libro.data_prestito = None
            libro.data_restituzione = data_restituzione
            return True
        return False

    def cerca_libro_per_titolo(self, titolo: str) -> List[Libro]:
        """Cerca libri per titolo"""
        return [libro for libro in self.libri if titolo.lower() in libro.titolo.lower()]

    def cerca_libri_per_autore(self, autore: Autore) -> List[Libro]:
        """Restituisce i libri di un determinato autore"""
        return [libro for libro in self.libri if libro.autore == autore]

    def libri_disponibili(self) -> List[Libro]:
        """Restituisce la lista dei libri attualmente disponibili"""
        return [libro for libro in self.libri if libro.disponibile()]


# Esempio di utilizzo
def main():
    # Creazione della biblioteca
    biblioteca = Biblioteca()

    # Creazione autori
    autore1 = Autore("Alessandro", "Manzoni")
    autore2 = Autore("Italo", "Calvino")

    # Creazione libri
    libro1 = Libro("I Promessi Sposi", date(1827, 1, 1), autore1)
    libro2 = Libro("Il barone rampante", date(1957, 1, 1), autore2)

    # Aggiunta libri alla biblioteca e agli autori
    autore1.aggiungi_libro(libro1)
    autore2.aggiungi_libro(libro2)
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)

    # Creazione utenti
    utente1 = Utente("Mario", "Rossi")
    utente2 = Utente("Laura", "Bianchi")

    # Aggiunta utenti alla biblioteca
    biblioteca.aggiungi_utente(utente1)
    biblioteca.aggiungi_utente(utente2)

    # Stampa dei libri disponibili
    print("Libri disponibili iniziali:", [str(l) for l in biblioteca.libri_disponibili()])

    # Prestito libro
    biblioteca.presta_libro(libro1, utente1, date.today())
    print(f"\nLibro '{libro1.titolo}' prestato a {utente1.nome} {utente1.cognome}")

    # Stampa dei libri disponibili dopo il prestito
    print("\nLibri disponibili dopo il prestito:", [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca per autore
    print(f"\nLibri di {autore1}:",
          [str(l) for l in biblioteca.cerca_libri_per_autore(autore1)])

    # Restituzione libro
    biblioteca.restituisci_libro(libro1, date.today())
    print(f"\nLibro '{libro1.titolo}' restituito")

    # Stampa dei libri disponibili dopo la restituzione
    print("\nLibri disponibili dopo la restituzione:", [str(l) for l in biblioteca.libri_disponibili()])

    # Ricerca libro per titolo
    libri_trovati = biblioteca.cerca_libro_per_titolo("Promessi")
    print(f"\nLibri trovati con titolo contenente 'Promessi':", [str(l) for l in libri_trovati])

    # Ottieni tutti i libri
    print("\nTutti i libri in biblioteca:", [str(l) for l in biblioteca.ottieni_libri()])

    # Ottieni tutti gli utenti
    print("\nTutti gli utenti in biblioteca:", [str(u) for u in biblioteca.ottieni_utenti()])


if __name__ == "__main__":
    main()
