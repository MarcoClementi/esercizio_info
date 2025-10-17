```Mermaid
erDiagram
    Negozio {
        int id PK
        string indirizzo
        string città
    }

    Dipendente {
        int id PK
        string nome
        string cognome
        int negozio_id FK
    }

    Album {
        int id PK
        string titolo
        string artista
        int anno_pubblicazione
        float prezzo
    }

    Artista {
        int id PK
        string nome
        string genere
    }

    Vendita {
        int id PK
        int dipendente_id FK
        int album_id FK
        date data_vendita
        float prezzo_vendita
    }


    Negozio ||--o{ Dipendente : "ha"
    Dipendente ||--o{ Vendita : "effettua"
    Album ||--o{ Vendita : "è venduto in"
    Artista ||--o{ Album : "crea"

