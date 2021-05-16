# Arkkitehtyyrikuvaus

## Rakenne

Ohejlma rakennetta kuvaava pakkauskaavio:

![pakkauskaavio](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/pakkauskaavio.png)

Pakkaus ui vastaa valikoista ja niiden visuaalisista komponenteista, pakkaus gamelogic sisältää sovelluksen/pelin logiikasta huolehtivat komponentit ja pakkaus repositories sisältää tiedon tallentamisesta vastuussa olevat toiminnallisuudet (tätä pakkausta ei vielä ole, koska projekti on vielä kesken).

## Käyttöliittymä

Peli sisältää viisi relilasta näkymää:

- Aloitusvalikko
- Pelaajien nimi valikko
- Peli historia
- Peli
- Lopetusnäkymä 

Alotusvalikosta pääsee joko pelaajien nimi valikkoon, peli historia näkymään tai vaihtoehtoisesti voi sulkea pelin. Pelaajien nimi valikossa kirjoitetaan pelaajien nimet, valitaan väri ja aloitetaan peli. Peli historia näkymässa voi tarkastella vanhojen pelien tuloksia (tämä toiminto ei ole vielä valmis).

Pelinäkymässä pelataan shakkia tuttuun tapaan. Pelinäkymä rakentuu useista luokista ja siitä vastaa gamelogic paketti. Pelin suorittamisesta vastaa `main` -funktio, joka kutsuu muiden luokkien metodeita siirtoja tehdessä.

Pelin loppuessa pelinäkymä sulkeutuu ja lopetusnäkymä tulee näkyviin joka kertoo pelin tuloksen. Lopetusnäkymästä on mahdollista palata takaisin päävalikkoon.

Kaikista näkymistä, paitsi pelinäkymästä, vastaa `ui` -luokka, joka asettaa aina pelaajan valitseman näkymän `current_view` -muuttujaan ja näyttää sen. Jokaiselle näkymälle on erikseen oma luokka, joka vastaa vain siitä näkymästä (lopetusnäkymä on vielä kahdessa eri luokassa, mutta ne tullaan yhdistämään).

## Tietojen tallentaminen

`MatchHistoryRepository` -luokka huolehtii tietojen tallentamisesta SQLite-tietokantaan. Tietokantaan tallennetaan jokaisen pelatun pelin jälkeen pelaajien nimet sekä pelin tulos.

### Tietokanta

Tietokantatiedoston nimi on määritelty [.env](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/shakki/.env) -tiedostossa, joten sen vaihtaminen on helppoa.

Tietokannassa tiedot tallennetaan `match_history` -tauluun, joka on seuraavanlainen:

| player1 | player2 |  result |
| :-----: | :-----: | :-----: |
| thuckey | makeri  |    1    |
| thuckey | makeri  |    2    |
| thuckey | makeri  |    3    |

Tietokanta alustetaan [initialize-db.py](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/shakki/src/initialize_db.py) -tiedostossa.

## Sovelluslogiikka

Sovelluslogiikan luokkakaavio on seuraavanlainen:

![luokkakaavio](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/luokkakaavio.png)

`GameState` -luokka vastaa pelin/laudan tilanteesta ja päivittää niitä pelin edetessä.
`Attack` -luokka luo ja päivittää 2D matriiseja ruuduista joita uhataan. Molemmilla väreillä on omat matriisit.
`Piece` -luokka vastaa kaikista nappuloiden toiminnallisuuksista.
`Result` -luokka tarkistaa onko peli ohi jokaisen siirron jälkeen.

Kaikki luokat tarvitsevat `GameState` -luokkaa, jotta ne pysyvät mukana laudan tilasta pelin edetessä. Luokat ovat erittäin sidoksissa toisiinsa ja kutsuvat toisiaan ainakin kerran per siirto. Poikkeus on `Result` -luokka joka vastaa vain pelin tuloksen tarkistamisesta joka siirron jälkeen.

## Toiminnallisuudet

Shakille tuttuun tapaan pelaajat tekevät siirtoja vuorotellen shakin sääntöjen mukaisesti.
Siirron jälkeen sovellus kysyy, onko shakkimatti alla näkyvällä tavalla.

![sekvenssikaavio](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/sekvenssikaavio.png)

`Piece` -luokka tarkistaa siirron jälkeen `Attack` -luokalta onko siirto aiheuttanut shakin. `Attack` -luokka kysyy kuninkaiden sijainnin `GameState` -luokalta ja tämän jälkeen tarkistaa onko shakki. Shakin ollessa `Attack` -luokka lähettää siitä tiedon `GameState` -luokalle ja kysyy `Result` -luokalta onko shakkimatti ja tämä vastaa True tai False riippuen onko vai ei.


Siirron logiikka on hyvin pitkä ja monimutkainen projekti, joten sen selittäminen on jätetty pois.


