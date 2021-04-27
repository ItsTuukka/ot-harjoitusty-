# Shakki

Simppeli shakki kahdelle pelaajalle, joka on toteutettu Pythonilla.

Peli on Ohjelmistotekniikan-kurssilla tehtävä projektityö.

Peli toimii Python-versiolla `3.7` tai uudemmalla, johtuen pelille välttämättömästä ulkoisesta kirjastosta.

### Release 1

-[Viikon 5 release](https://github.com/ItsTuukka/ot-harjoitusty-/releases/tag/viikko5)

Pelkästään peli toimii, käyttöliittymää muulle kuin pelinäkymälle ei ole.
Shakkimatti, patti, liian vähän nappuloita, viisinkertainen toisto päättää pelin ja sulkee sovelluksen.
Pelin tulos tulee näkyviin komentoriville.

### Dokumentaatio

- [Vaativuusmäärittely](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/vaatimuusm%C3%A4%C3%A4rittely.md)
- [Arkkitehtuurikuvaus](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)

### Asennus

1. Siirry komentorivillä shakki kansioon.

2. Asenna riippuvuudet komennolla

```
poetry install
```

3. Käynnistä sovellus komennolla

```
poetry run invoke start
```

### Komentorivikomennot

#### Ohjelman voi suorittaa komennolla

```
poetry run invoke start
```

#### Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

#### Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage-report
```

Raportti generoituu shakki/htmlcov/index.html tiedostoon.

#### Pylint tarkistus komennolla

```
poetry run invoke lint
```
