# Tekstiseikkailu


Yksinkertainen tekstipohjainen seikkailupeli, jossa pelaaja voi liikkua huoneiden välillä ja kerätä esineitä.

## Projektin rakenne

projekti/ │ ├── main.py ├── pelaaja.py │ ├── room.py │ └── items.py │ └── tools/ └── main.py

### Moduulit

#### esine.py
Sisältää `Esine`-luokan.

Esineellä on:
- nimi
- paino

#### huone.py
Sisältää `Huone`-luokan.

Huoneella on:
- nimi
- lista huoneessa olevista esineistä

#### pelaaja.py
Sisältää `Pelaaja`-luokan.

Pelaajalla on:
- nimi
- sijainti (nykyinen huone)
- inventaario (kerätyt esineet)

Toiminnot:
- liikkuminen huoneesta toiseen
- esineiden kerääminen

#### peli.py
Sisältää pelin päälogiikan ja valikot.

#### main.py
Ohjelman käynnistyspiste.

## Luokat

### Esine

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| paino | float |

### Huone

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| esineet | list |

### Pelaaja

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| esineet | list |
| sijainti | Huone |

### Metodit

#### Pelaaja.liiku(kohde)

Siirtää pelaajan annettuun huoneeseen.

#### Pelaaja.keraa_esine(esine)

Lisää esineen pelaajan inventaarioon ja poistaa sen huoneesta.

## Ohjelman toiminta

1. Ohjelma luo käynnistyessään:
   - pelaajaolion
   - vähintään yhden huoneen
   - muutaman esineen

2. Pelaaja voi:
   - liikkua huoneiden välillä
   - tarkastella inventaariotaan
   - kerätä esineitä

3. Pelivalikko toistuu, kunnes käyttäjä lopettaa ohjelman.

## UML-kaavio

Projektin luokkarakenne:

- Pelaaja omistaa 0..* esinettä.
- Pelaaja sijaitsee yhdessä huoneessa.
- Huone sisältää 0..1 esineen (tai useita toteutuksesta riippuen).
- Esineellä on nimi ja paino.

## Esimerkkikäyttö


Liiku
Kerää esine
Näytä inventaario
Lopeta

Valinta: 2

Keräsit esineen: Avain

## Tekijä
Petri Kettunen