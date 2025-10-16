```Mermaid
erDiagram
    AZIENDA {
        int partita_iva PK
        string nome
        string via
        int numero_civico
        string comune
        string provincia
        string regione
    }
    VIGNETO {
        int codice_vigneto PK
        string nome
        float superficie_ha
        string localita
        string comune
        string classe_esposizione
        int num_filari
        int partita_iva_FK
    }
    BLOCCO {
        int codice_blocco PK
        float superficie_ha
        string classe_esposizione
        int codice_vigneto_FK
    }
    VITIGNO {
        string nome_scientifico PK
        string nome_comune
        string colore
        string origine_genetica
    }
    COLTIVAZIONE {
        int codice_blocco_FK PK
        string nome_scientifico_FK PK
        float percentuale_superficie
    }
    ETICHETTA {
        int id_etichetta PK
        string nome
        int annata
        string tipologia
        int partita_iva_FK
        int codice_vigneto_principale_FK
        string vitigno_prevalente_FK
    }

    AZIENDA ||--o{ VIGNETO : possiede
    VIGNETO ||--o{ BLOCCO : "è_suddiviso_in"
    BLOCCO ||--o{ COLTIVAZIONE : "ha"
    VITIGNO ||--o{ COLTIVAZIONE : "è_piantato_in"
    AZIENDA ||--o{ ETICHETTA : produce
    VIGNETO ||--o{ ETICHETTA : "vigneto_principale_per"
    VITIGNO ||--o{ ETICHETTA : "vitigno_prevalente_per"
```