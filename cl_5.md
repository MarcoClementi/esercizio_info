```mermaid
    erDiagram
AUTORE {
    string ID
    string nome
    string cognome
}
LIBRO {
    string ID
    string titolo
    string autore_id
    int anno
    string genere
    }

PRESTITO {
    string ID
    string libro_id
    string utente
    string data_prestito
    string data_restituzione
    }

    AUTORE {|-- LIBRO : "scrive"
    LIBRO |-- PRESTITO : "è prestato in"
    AUTORE ||--o PRESTITO : "ha prestato"
    AUTORE ||-- AUTORE : "collabora con"
```
