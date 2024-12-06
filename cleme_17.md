```Mermaid
classDiagram
    class Insegnante {
        +string nome
        +string cognome
        +string strumento
        +List<Studente> studenti
        +aggiungi_studente() -->Void 
    }

    class Studente {
        +string nome
        +string cognome
        +Insegnante insegnante
        +List<Corso> corsi
        +set_Insegnante(insegnante: Insegnante)
        +iscrivi_Corso(corso: Corso)
    }

    class Corso {
        +string nome
        +string durata
        +aggiungiStudente(studente: Studente)
    }

    Insegnante "1" -- "*" Studente : insegna_a
    Studente "*" -- "*" Corso : iscrizione_a
