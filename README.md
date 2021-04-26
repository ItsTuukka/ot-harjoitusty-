# Shakki

Simppeli shakki kahdelle pelaajalle, joka on toteutettu Pyhonilla.

Peli on Ohjelmistotekniikan-kurssilla tehtävä projektityö.

Peli toimii Python-versiolla `3.6` tai uudemmalla.

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

#### Pylint tarkistus komennolla

```
poetry run invoke lint
```
