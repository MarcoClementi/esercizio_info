CREATE TABLE Typology (
    id INT PRIMARY KEY,
    typology_name VARCHAR(50),
    typology_description TEXT
);

CREATE TABLE Beekeeper (
    id INT PRIMARY KEY,
    beekeeper_name VARCHAR(100)
);

CREATE TABLE Honey (
    id INT PRIMARY KEY,
    denomination VARCHAR(100),
    typology_id INT,
    FOREIGN KEY (typology_id) REFERENCES Typology(id)
);

CREATE TABLE Apiary (
    code VARCHAR(10) PRIMARY KEY,
    num_hives INT,
    locality VARCHAR(100),
    comune VARCHAR(100),
    province VARCHAR(100),
    region VARCHAR(100),
    beekeeper_id INT,
    FOREIGN KEY (beekeeper_id) REFERENCES Beekeeper(id)
);

CREATE TABLE Production (
    id INT PRIMARY KEY,
    year INT,
    quantity FLOAT,
    apiary_code VARCHAR(10),
    honey_id INT,
    FOREIGN KEY (apiary_code) REFERENCES Apiary(code), 
    FOREIGN KEY (honey_id) REFERENCES Honey(id) 
);
--Foreign key = chiave esterna (colonna che fa riferimento a un'altra tabella)
--Primary key = chiave primaria (colonna che identifica univocamente una riga in una tabella
-- Typology
INSERT INTO Typology (id, typology_name, typology_description) VALUES
(1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
(2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
(3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

-- Beekeeper
INSERT INTO Beekeeper (id, beekeeper_name) VALUES
(1, 'Marco Rossi'),
(2, 'Lucia Bianchi'),
(3, 'Alessandro Verdi');

-- Honey
INSERT INTO Honey (id, denomination, typology_id) VALUES
(1, 'Acacia', 1),
(2, 'Castagno', 1),
(3, 'Millefiori', 2),
(4, 'Eucalipto', 2),
(5, 'Melata di Bosco', 3);

-- Apiary
INSERT INTO Apiary (code, num_hives, locality, comune, province, region, beekeeper_id) VALUES
('100', 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
('101', 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
('102', 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
('103', 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

-- Production
INSERT INTO Production (id, year, quantity, apiary_code, honey_id) VALUES 
(1, 2022, 120.5, '100', 1),
(2, 2022, 95.2, '101', 3),
(3, 2023, 210.0, '102', 5),
(4, 2023, 34.7, '103', 2),
(5, 2024, 150.0, '100', 3),
(6, 2024, 78.3, '101', 4);

SELECT * FROM Beekeeper; -- Visualizza tutti gli apicoltori
SELECT beekeeper_name FROM Beekeeper WHERE id = 1; -- Nome dell'apicoltore con id 1
SELECT * FROM Apiary WHERE region = 'Lombardia'; -- Apiari in Lombardia
SELECT code, num_hives FROM Apiary WHERE num_hives > 10; -- Apiari con più di 10 arnie
SELECT code, locality FROM Apiary WHERE beekeeper_id = 2; -- Apiari dell'apicoltore con id 2
SELECT * FROM Honey WHERE typology_id = 3; -- Mieli di tipo Honeydew
SELECT denomination FROM Honey WHERE id = 5; -- Denominazione del miele con id 5
SELECT * FROM Production WHERE year = 2024; -- Produzioni dell'anno 2024


--FROM = indica la tabella da cui prelevare i dati
--SELECT = indica le colonne da visualizzare
--WHERE = indica le condizioni che devono essere soddisfatte per visualizzare i dati
