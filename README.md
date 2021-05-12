# Shakki

Simppeli shakki kahdelle pelaajalle, joka on toteutettu Pythonilla.

Peli on Ohjelmistotekniikan-kurssilla tehtävä projektityö.

Peli toimii Python-versiolla `3.7` tai uudemmalla.

### Lataa sovellus täältä

[Viikon 6 release](https://github.com/ItsTuukka/ot-harjoitusty-/releases/tag/viikko6)

### Dokumentaatio

- [Vaativuusmäärittely](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/vaatimuusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)
- [Käyttöohje](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kayttoohje.md)

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
