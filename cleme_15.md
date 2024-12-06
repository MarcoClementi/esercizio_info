```Mermaid
   
  %%% Diagramma del Sistema di Gestione Biblioteca
classDiagram
    %% Definizione della classe Autore con i suoi attributi
    class Autore {
        -String nome
        -String cognome
    }
    
    %% Definizione della classe Biografia con i suoi attributi
    class Biografia {
        -String testo
        -Data dataPubblicazione
    }
    
    %% Definizione della classe Biblioteca con i suoi attributi
    class Biblioteca {
        -String nome
        -String indirizzo
    }
    
    %% Definizione della classe Libro con il suo attributo
    class Libro {
        -String titolo
    }
    
    %% Definizione della classe Studente con i suoi attributi
    class Studente {
        -String nome
        -String cognome
    }
    
    %% Definizione della classe base Dispositivo
    class Dispositivo {
        -String marca
        -String modello
    }
    
    %% Definizione delle classi che ereditano da Dispositivo
    class Smartphone {
        -Bool supporta5G
    }
    
    class Tablet {
        -Bool haPenna
    }
    
    %% Relazioni di ereditarietà (inheritance)
    %% La freccia vuota indica che Smartphone e Tablet ereditano da Dispositivo
    Dispositivo <|-- Smartphone
    Dispositivo <|-- Tablet
    
    %% Relazioni one-to-one e one-to-many per Autore
    %% "1" -- "1" indica relazione one-to-one
    %% "1" -- "*" indica relazione one-to-many
    Autore "1" -- "1" Biografia : scrive >
    Autore "1" -- "*" Libro : scrive >
    
    %% Relazioni one-to-many per Biblioteca
    Biblioteca "1" -- "*" Libro : contiene >
    Biblioteca "1" -- "*" Studente : serve >
    
    %% Relazione many-to-many tra Libro e Studente (per i prestiti)
    %% "*" -- "*" indica che molti libri possono essere prestati a molti studenti
    Libro "*" -- "*" Studente : prestato a >
    
    %% Relazione one-to-one tra Studente e Dispositivo
    Studente "1" -- "1" Dispositivo : possiede >