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

Pelinäkymässä pelataan shakkia tuttuun tapaan. Pelinäkymä rakentuu useista luokista ja siitä vastaa gamelogic paketti. Pelin suorittamisesta vastaa 'main' -funktio, joka kutsuu muiden luokkien metodeita siirtoja tehdessä.

Pelin loppuessa pelinäkymä sulkeutuu ja lopetusnäkymä tulee näkyviin joka kertoo pelin tuloksen. Lopetusnäkymästä on mahdollista palata takaisin päävalikkoon.

Kaikista näkymistä, paitsi pelinäkymästä, vastaa 'ui' -luokka, joka asettaa aina pelaajan valitseman näkymän 'current_view' -muuttujaan ja näyttää sen. Jokaiselle näkymälle on erikseen oma luokka, joka vastaa vain siitä näkymästä (lopetusnäkymä on vielä kahdessa eri luokassa, mutta ne tullaan yhdistämään).

## Tietojen tallentaminen

Tulossa hyvin pian.

## Sovelluslogiikka

Sovelluslogiikan luokkakaavio on seuraavanlainen:

![luokkakaavio](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/luokkakaavio.png)

Kaikki luokat tarvitsevat 'GameState' -luokkaa, jotta ne pysyvät mukana laudan tilasta pelin edetessä. Luokat ovat erittäin sidoksissa toisiinsa ja kutsuvat toisiaan ainakin kerran per siirto. Poikkeus on 'Result' -luokka joka vastaa vain pelin tuloksen tarkistuksesta aina siirron jälkeen

## Toiminnallisuudet

Shakille tuttuun tapaan pelaajat tekevät siirtoja vuorotellen shakin sääntöjen mukaisesti.
Siirron jälkeen sovellus kysyy, onko shakkimatti alla näkyvällä tavalla.

![sekvenssikaavio](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/sekvenssikaavio.png)

'Piece' -luokka tarkistaa siirron jälkeen 'Attack' -luokalta onko siirto aiheuttanut shakin. 'Attack' -luokka kysyy kuninkaiden sijainnin 'GameState' -luokalta ja tämän jälkeen tarkistaa onko shakki. Shakin ollessa 'Attack' -luokka lähettää siitä tiedon 'GameState' -luokalle ja kysyy 'Result' -luokalta onko shakkimatti ja tämä vastaa True tai False riippuen onko vai ei.

Siirron logiikka on hyvin pitkä ja monimutkainen projekti (johtuen myös omasta osaamisesta, tai sen puutteesta), joten sen selittäminen on jätetty pois.
