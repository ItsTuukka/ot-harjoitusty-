# Testausdokumentti

Peli on testtu yksikkö- ja integraatiotesteillä unittestiä käyttäen.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Pelin sekä laudan tilasta vastaavaaa `GameState`-luokkaa testataan omassa luokassaan. `TestGameState` -testiluokka testaa vuoron vaihtumista, eri laudan tilanteita sekä
attribuuttien päivittymistä pelin edetessä.

`Piece` luokka testataan omassa "TestPieces" luokassa, mutta tämä vaatii kaikkien muiden luokkien luomista toimiakseen. Testiluokka testaa linnottautumista, enpassanttia sekä
eri nappuloiden liikkumista.

`Attack` luokka testataan omassa "TestAttack" luokassa, mutta tämä vaatii kaikkien muiden luokkien luomista toimiakseen. Testiluokka testaa 2D uhkausmatriiseja sekä 
`check_after` -funktiota, joka varmistaa että siirto ei saata omaa kuningasta shakkiin.

### Repositoria-luokka

Tietojen pysyväistallennuksesta vastaavaa `MatchHistoryRepository` -luokkaa testataan omalla `TestDatabase` -testiluokalla. 
Testeissä käytetään oma testitietokantaa, joka on määritelty .env.test-tiedostossa. Luokan kaikkia metodeita testataan erikseen.

## Testikattavuus

Testien haarautumakattavuus on 70%

![coverage](https://github.com/ItsTuukka/ot-harjoitusty-/blob/master/dokumentaatio/kuvat/coverage.png)

Testien ulkopuolelle on jäänyt `main` -tiedosto, josta löytyy `main` -funktio pygamen ja sen tapahtumisien pyörittämiseen, `end_game` -funktio, joka vastaa pelin jälkeisistä tapahtumista ja
`draw_board` -funktio, joka vastaa laudan piirtämisestä.

## Järjestelmätestaus

Sovellusta on testattu järjestelmätasolla manuaalisesti.

### Asennus ja konfigurointi

Pelin käyttöä on testattu sekä omalla koneella, jossa on käytössä Cubbli, että yliopiston virtuaalikoneella asentamalla se käyttöohjeen kuvaamalla tavalla.

Pelin toimintaa on testattu pelaamalla eri skenaarioita läpi ja varsinkin kaikki "erikois" toiminnot kuten linnottautuminen on testattu monella variaatiolla.

Sovelluksen kaatavia bugeja ei ole löytynyt, mutta pelin luonteen takia on mahdotonta testata jokaista mahdollista skenaariota. Myös "Match History" näkymä jättää toivomisen varaa,
kun tietokannassa ei ole yhtään peliä tallennettuna. 
