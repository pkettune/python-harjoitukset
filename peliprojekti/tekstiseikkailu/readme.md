# Tekstiseikkailu

Yksinkertainen tekstipohjainen room escape, jossa pelaaja voi liikkua huoneiden välillä ja kerätä esineitä.

Tavoitteena on ottaa itseään niskasta kiinni ja lähteä levittämään tasa-arvoa.

## Projektin rakenne

├──peliprojekti
   ├──tekstiseikkailu
      ├──main.py
      ├──player.py
      ├──room.py
      ├──items.py
      ├──tools.py
      ├──intro.txt
      ├──ohjeet.txt
      ├──save.ext


### Moduulit

#### main.py
Sisältää pelin päälogiikan, ohjelman käynnistyspiste.

#### tools.py
Sisältää datan tallennuksen ja latauksen, sekä clear_screen()

#### items.py
Sisältää `Item`-luokan.

Esineellä on:
- nimi
- paino

#### room.py
Sisältää `Room`-luokan.

Huoneella on:
- nimi
- kerättävä tavara (item, jos on)

#### player.py
Sisältää `Player`-luokan.

Pelaajalla on:
- nimi (name)
- kerätyt esineet (items)
- sijainti (location)
- kerättyjen tavaroiden yhteispaino (itemLoad)

Toiminnot:
- liikkuminen huoneesta toiseen (move)
- esineiden kerääminen (collect_item)
- näytä kerättyjen esineiden lista (show_items)
- käytä esinettä (use_item)
- nimen vaihtaminen (change_name)
- katso huonetta jossa olet (look_around)


## Luokat

### Pelaaja

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| esineet | list |
| sijainti | Huone |
| tavaroiden yhteispaino | int |

### Huone

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| esineet | list |

### Esine

| Ominaisuus | Tyyppi |
|------------|---------|
| nimi | str |
| paino | float |


## Ohjelman toiminta

1. Ohjelma luo käynnistyessään:
   - pelaajaolion
   - 5 huonetta
   - 5 esinettä

2. Pelaaja voi:
   - liikkua huoneiden välillä
   - tarkastella inventaariotaan
   - tarkatella ympärillensä
   - kerätä esineitä
   - käyttää esineitä

3. Pelivalikko toistuu, kunnes käyttäjä lopettaa ohjelman.

4. Pelin tallennus ja lataus.


## Tekijä
Petri Kettunen