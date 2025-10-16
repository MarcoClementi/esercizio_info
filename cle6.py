import sqlite3
from typing import List, Tuple

# Connessione al database SQLite 'libreria.db'
conn: sqlite3.Connection = sqlite3.connect("libreria.db")
cursor: sqlite3.Cursor = conn.cursor()

def create_tables():
    """Crea le tabelle se non esistono."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Autori (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cognome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Libri (
            id INTEGER PRIMARY KEY,
            titolo TEXT NOT NULL,
            autore_id INTEGER,
            anno INTEGER,
            genere TEXT,
            FOREIGN KEY (autore_id) REFERENCES Autori(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Prestiti (
            id INTEGER PRIMARY KEY,
            libro_id INTEGER,
            utente TEXT NOT NULL,
            data_prestito TEXT,
            data_restituzione TEXT,
            FOREIGN KEY (libro_id) REFERENCES Libri(id)
        )
    """)
    conn.commit()

def insert_data():
    """Inserisci i dati di esempio."""
    # Autori
    autori = [
        (1, 'Mario', 'Rossi'),
        (2, 'Lucia', 'Bianchi'),
        (3, 'Alessandro', 'Verdi')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Autori (id, nome, cognome) VALUES (?, ?, ?)", autori)

    # Libri
    libri = [
        (1, 'Il mistero del castello', 1, 2020, 'Giallo'),
        (2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza'),
        (3, 'La cucina italiana', 2, 2019, 'Cucina'),
        (4, 'Storia antica', 3, 2021, 'Storia'),
        (5, 'Romanzo moderno', 3, 2022, 'Narrativa'),
        (6, 'Il ritorno del castello', 1, 2023, 'Giallo')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)", libri)

    # Prestiti
    prestiti = [
        (1, 1, 'Mario Rossi', '2023-01-01', '2023-01-15'),
        (2, 2, 'Lucia Bianchi', '2023-02-01', None),
        (3, 3, 'Alessandro Verdi', '2023-03-01', '2023-03-10'),
        (4, 4, 'Mario Rossi', '2023-04-01', None)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)", prestiti)
    conn.commit()

def query_libri_per_autore(autore_id: int) -> List[Tuple[int, str, int, str]]:
    """Restituisce tutti i libri di un autore specifico (usa JOIN)."""
    cursor.execute("""
        SELECT Libri.id, Libri.titolo, Libri.anno, Libri.genere
        FROM Libri
        JOIN Autori ON Libri.autore_id = Autori.id
        WHERE Autori.id = ?
    """, (autore_id,))
    return cursor.fetchall()

def query_prestiti_per_utente(utente: str) -> List[Tuple[int, str, str, str]]:
    """Restituisce i prestiti di un utente (usa JOIN)."""
    cursor.execute("""
        SELECT Prestiti.id, Libri.titolo, Prestiti.data_prestito, Prestiti.data_restituzione
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
        WHERE Prestiti.utente = ?
    """, (utente,))
    return cursor.fetchall()

def query_libri_per_genere() -> List[Tuple[str, int]]:
    """Restituisce il numero di libri per genere (usa GROUP BY)."""
    cursor.execute("""
        SELECT genere, COUNT(*) AS num_libri
        FROM Libri
        GROUP BY genere
    """)
    return cursor.fetchall()

def query_autori_con_piu_libri() -> List[Tuple[str, str, int]]:
    """Restituisce gli autori ordinati per numero di libri (usa JOIN, GROUP BY, ORDER BY)."""
    cursor.execute("""
        SELECT Autori.nome, Autori.cognome, COUNT(*) AS num_libri
        FROM Autori
        JOIN Libri ON Autori.id = Libri.autore_id
        GROUP BY Autori.id
        ORDER BY num_libri DESC
    """)
    return cursor.fetchall()

def query_prestiti_non_restituiti() -> List[Tuple[int, str, str, str]]:
    """Restituisce i prestiti non ancora restituiti (data_restituzione IS NULL)."""
    cursor.execute("""
        SELECT Prestiti.id, Libri.titolo, Prestiti.utente, Prestiti.data_prestito
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
        WHERE Prestiti.data_restituzione IS NULL
    """)
    return cursor.fetchall()

#Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN). 
def query_tutti_i_libri() -> List[Tuple[str, int, str]]:
    """Restituisce tutti i libri con titolo, anno e nome dell'autore (usa JOIN)."""
    cursor.execute("""
        SELECT Libri.titolo, Libri.anno, Autori.nome || ' ' || Autori.cognome AS autore
        FROM Libri
        JOIN Autori ON Libri.autore_id = Autori.id
    """)
    return cursor.fetchall()

#Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN).
def query_tutti_i_prestiti() -> List[Tuple[str, str, str]]:
    """Restituisce tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN)."""
    cursor.execute("""
        SELECT Libri.titolo, Prestiti.utente, Prestiti.data_prestito
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
    """)
    return cursor.fetchall()

#Libri pubblicati dopo il 2020. Risultato
def query_libri_dopo_2020() -> List[Tuple[int, str, int]]:
    """Restituisce i libri pubblicati dopo il 2020."""
    cursor.execute("""
        SELECT id, titolo, anno
        FROM Libri
        WHERE anno > 2020
    """)
    return cursor.fetchall()

#Numero di prestiti per ciascun utente (usa GROUP BY).
def query_numero_prestiti_per_utente() -> List[Tuple[str, int]]:
    """Restituisce il numero di prestiti per ciascun utente (usa GROUP BY)."""
    cursor.execute("""
        SELECT utente, COUNT(*) AS num_prestiti
        FROM Prestiti
        GROUP BY utente
    """)
    return cursor.fetchall()

#Libri ordinati per genere e poi per anno (usa ORDER BY multiplo). 
def query_libri_ordinati_per_genere_e_anno() -> List[Tuple[str, int, str]]:
    """Restituisce i libri ordinati per genere e poi per anno (usa ORDER BY multiplo)."""
    cursor.execute("""
        SELECT titolo, anno, genere
        FROM Libri
        ORDER BY genere, anno
    """)
    return cursor.fetchall()

#Prestiti restituiti (dove data_restituzione non è NULL)
def query_prestiti_restituiti() -> List[Tuple[int, str, str, str]]:
    """Restituisce i prestiti restituiti (dove data_restituzione non è NULL)."""
    cursor.execute("""
        SELECT Prestiti.id, Libri.titolo, Prestiti.utente, Prestiti.data_restituzione
        FROM Prestiti
        JOIN Libri ON Prestiti.libro_id = Libri.id
        WHERE Prestiti.data_restituzione IS NOT NULL
    """)
    return cursor.fetchall()

#Autori e numero di libri, inclusi quelli senza libri (usa LEFT JOIN e GROUP BY). 
def query_autori_e_numero_di_libri() -> List[Tuple[str, str, int]]:
    """Restituisce autori e numero di libri, inclusi quelli senza libri (usa LEFT JOIN e GROUP BY)."""
    cursor.execute("""
        SELECT Autori.nome, Autori.cognome, COUNT(Libri.id) AS num_libri
        FROM Autori
        LEFT JOIN Libri ON Autori.id = Libri.autore_id
        GROUP BY Autori.id
    """)
    return cursor.fetchall()


# Codice principale
if __name__ == "__main__":
    try:
        create_tables()
        insert_data()
        print("Database creato e dati inseriti con successo.\n")

        # Query 3: Libri per autore (es. autore_id=1)
        print("3) Libri dell'autore con id 1:")
        libri_autore = query_libri_per_autore(1)
        for libro in libri_autore:
            print(f"ID: {libro[0]}, Titolo: {libro[1]}, Anno: {libro[2]}, Genere: {libro[3]}")
        print()

        # Query 4: Prestiti per utente (es. 'Mario Rossi')
        print("4) Prestiti dell'utente 'Mario Rossi':")
        prestiti_utente = query_prestiti_per_utente('Mario Rossi')
        for prestito in prestiti_utente:
            print(f"ID Prestito: {prestito[0]}, Titolo Libro: {prestito[1]}, Data Prestito: {prestito[2]}, Data Restituzione: {prestito[3]}")
        print()

        # Query 5: Libri per genere
        print("5) Numero di libri per genere:")
        libri_genere = query_libri_per_genere()
        for genere in libri_genere:
            print(f"Genere: {genere[0]}, Numero libri: {genere[1]}")
        print()

        # Query 6: Autori con più libri
        print("6) Autori ordinati per numero di libri:")
        autori_libri = query_autori_con_piu_libri()
        for autore in autori_libri:
            print(f"Nome: {autore[0]}, Cognome: {autore[1]}, Numero libri: {autore[2]}")
        print()

        # Query 7: Prestiti non restituiti
        print("7) Prestiti non ancora restituiti:")
        prestiti_non_restituiti = query_prestiti_non_restituiti()
        for prestito in prestiti_non_restituiti:
            print(f"ID Prestito: {prestito[0]}, Titolo Libro: {prestito[1]}, Utente: {prestito[2]}, Data Prestito: {prestito[3]}")

    finally:
        # Chiusura connessione
        conn.close()
        print("\nConnessione chiusa.")