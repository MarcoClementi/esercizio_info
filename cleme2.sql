-- Creazione delle tabelle per la gestione degli apicoltori, tipologie di miele, apiari e produzione di miele

CREATE TABLE BEEKEEPER (                          
    id INT IDENTITY(1,1) PRIMARY KEY, 
    name NVARCHAR(100) NOT NULL,
    id_apicoltore INT
);

CREATE TABLE TYPOLOGY (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    description NVARCHAR(255)
);

CREATE TABLE HONEY (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    id_typology INT,
    denomination NVARCHAR(255)
);

CREATE TABLE APIARY (
    id_beekeeper INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    code NVARCHAR(50) UNIQUE,
    location NVARCHAR(255),
    num_hives INT,
    comune NVARCHAR(100),
    province NVARCHAR(100),
    region NVARCHAR(100)
);


CREATE TABLE PRODUCTION (   -- Produzione di miele
    id INT IDENTITY(1,1) PRIMARY KEY, -- Identificativo univoco della produzione
    id_honey INT, -- Riferimento al tipo di miele prodotto
    id_apiary INT, -- Riferimento all'apiario dove è avvenuta la produzione
    year INT, -- Anno della produzione
    quantity DECIMAL(10,2) -- Quantità di miele prodotta in kg
);
-- Inserire apicoltore
INSERT INTO BEEKEEPER (name, id_apicoltore) VALUES ('Giovanni Verdi', 1);
INSERT INTO BEEKEEPER (name, id_apicoltore) VALUES ('Anna Neri', 2);

-- Inserire tipologie di miele
INSERT INTO TYPOLOGY (name, description) VALUES ('Millefiori', 'Miele prodotto da diverse specie di fiori');
INSERT INTO TYPOLOGY (name, description) VALUES ('Acacia', 'Miele chiaro e delicato prodotto dai fiori di acacia');

-- Inserire tipi di miele
INSERT INTO HONEY (name, id_typology, denomination) VALUES ('Miele di Millefiori', 1, 'Denominazione di origine protetta');
INSERT INTO HONEY (name, id_typology, denomination) VALUES ('Miele di Acacia', 2, 'Denominazione di origine protetta');
