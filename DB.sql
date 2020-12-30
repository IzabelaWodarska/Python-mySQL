CREATE DATABASE hotel;

CREATE TABLE Goscie
(
    Gosc_id      INT         PRIMARY KEY AUTO_INCREMENT,
    Imię         VARCHAR(30) NOT NULL,
    Nazwisko     VARCHAR(30) NOT NULL,
    Adres        VARCHAR(30) NOT NULL,
    Kod          VARCHAR(6)  NOT NULL,
    Miasto       VARCHAR(15) NOT NULL,
    Kraj         VARCHAR(15) NOT NULL,
    Paszport     VARCHAR(15) NOT NULL UNIQUE,
    Telefon      INT(12)     NOT NULL,
    Przyjazd     DATE        NOT NULL,
    Wyjazd       DATE        NOT NULL,
    Nr_Pokoju    INT(3)      NOT NULL,
    Ilosc_Gosci  SMALLINT    NOT NULL,
    Ilosc_Nocy   SMALLINT    NOT NULL,
    Cena         FLOAT(6,2)  CHECK(Cena>=1),
    Platnosc     VARCHAR(10) NOT NULL,
    Uwagi        VARCHAR(300)
);