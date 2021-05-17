# Käyttöohje

Lataa projektin viimeisin [release](https://github.com/ItsTuukka/ot-harjoitusty-/releases/tag/1.0.0) itsellesi.

Siirry komentorivillä projektista löytyvään shakki -kansioon ja suorita kaikki ohjelmaan liittyvät komennot sieltä.

## Konfigurointi

Pelien tulokset tallennetaan sqlite-tietokantaan. Voit halutessasi vaihtaa tuon paikallisen tietokantatiedoston nimeä muokkaamalla shakki -kansiosta löytyvää .env -tiedostoa, mutta suosittelen kuitenkin säilyttämään data/ -alkuliitteen nimessä, jolloin tiedosto pysyy data -kansiossa. Oletuksena tiedoston sisältö on seuraavanlainen:

```
DB=data/db.sqlite
```

## Ohjelman käynnistäminen

Ennen pelin ensimmäistä käynnistystä suorita seuraavat komennot

```
poetry install
```

```
poetry run invoke initialize-db
```

Tämän jälkeen pelin voi käynnistää komennolla 

```
poetry run invoke start
```

## Pelin aloittaminen

Peli käynnistyy päävalikkoon:

![mainmenu](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/new_mainmenu.png)

Painamalla "Start Game" -painiketta pääset syöttämään pelaajien nimet.

![usernames](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/usernames.png)

Tämän jälkeen paina "Start" -painiketta aloittaaksesi peli.

## Pelin pelaaminen

Peliympäristö näyttää seuraavalta:

![pelinäkymä](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/pelin%C3%A4kym%C3%A4.png)

Peliä pelataan shakille tuttuun tapaan vuorotellen siirtoja tehden alkaen valkoisen vuorosta. Vain lailliset siirrot ovat sallittuja, eikä peli rekisteröi muita siirtoja.
Painamalla nappulaa valitset kyseisin nappulan ja painamalla nappulalle laillista ruutua teet siirron. Painamalla nappulaa uusiksi poistat sen hetkisen valintasi.

Kun peli päättyy, joko shakkimattiin tai erinäisiin tasapeli skenaarioihin, niin peli ikkuna sulkeutuu ja lopetusruutu tulee näkyviin kertoen pelin tuloksen.

![winscreen](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/winscreen.png)

Tästä voi palta takaisin päävalikkoon painamalla "Back to main menu" -painiketta tai lopettaa pelin painamalla rastia.

## Pelattujen pelien tarkastelu

Pelaajien käyttäjänimet sekä pelin tulos tallentuu tietokantaan. Pelattuja pelejä voi tarkastella päävalikosta painamalla "Match History" -painiketta.
Peli historia avautuu omaan ikkunaan ja näyttää seuraavalta:

![match_history](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/match_history.png)

Pelatut pelit näkyvät järjestyksessä aina uusin ylimpänä.
