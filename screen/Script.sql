CREATE TABLE Meldunki
(
    Meldunek_id     INT         PRIMARY KEY AUTO_INCREMENT,
    Przyjazd		DATETIME    NOT NULL,
    Wyjazd			DATETIME    NOT NULL,
    Nr_Pokoju		INT         NOT NULL,
    Ilosc_Gosci		SMALLINT    NOT NULL,
    Ilosc_Nocy		SMALLINT    NOT NULL,
    Cena			INT         NOT NULL,
    Platnosc		FLOAT(6,2)  CHECK(Platnosc>=1)
);
CREATE TABLE Goscie
(
    Gosc_id      INT         AUTO_INCREMENT,
    Meldunek_id  INT 	     NOT NULL,
    Imię         VARCHAR(30) NOT NULL,
    Nazwisko     VARCHAR(30) NOT NULL,
    Adres        VARCHAR(30) NOT NULL,
    Kod          INT         NOT NULL,
    Miasto       VARCHAR(30) NOT NULL,
    Kraj         VARCHAR(30) NOT NULL,
    Paszport     VARCHAR(30) NOT NULL UNIQUE,
    Telefon      INT         NOT NULL,
    PRIMARY KEY(Gosc_id), 
    FOREIGN KEY(Meldunek_id) REFERENCES Meldunki(Meldunek_id)
);

SELECT * FROM Meldunki;
SELECT * FROM Goscie;