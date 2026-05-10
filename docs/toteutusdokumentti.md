# Toteutusdokumentti
### Ohjelman yleisrakenne
Ohjelma on tehty Pythonilla ja käyttöliittymä Flaskilla. Siinä on toteuttettu A*- ja Jump Point Search (JPS) -hakualgoritmit. Ohjelmaan voidaan syöttää map-tiedosto sekä lähtö- ja maalipiste. Se palautta lyhimmän reitin sekä sen löytämiseen käytetyn ajan. Lisäksi se piirtää ASCII kartan, jossa näkyy kyseinen polku sekä kaikki vieraillut solmut.

JPS:n toteutus erosi alkuperäisestä paperista jokseenkin. Siinä esimerkiksi solmusta (0, 0) voi siirtyä solmuun (1, 1), jos joko (0, 1) tai (1, 0) on vapaa. Sovelluksessa sekä (0, 1) että (1, 0) solmujen täytyy olla liikuttavissa. Tämän tarkoitus on mahdollistaa on Moving AI Lab -sivuilla tarjottujen scen-tiedostojen käyttö testauksessa.

### Suorituskyky
Odotetusti JPS pärjäsi paremmin isoissa ja avoimmissa kaupunkipohjaisissa kartoissa, kuten `Berlin_1_256` ja `London_2_256`. Kartoissa, joissa on monta pientä estettä, JPS suoriutui heikommin kuin A* - esim. `brc000d`.

### Puutteet ja parannukset
Scen-tiedostojen testaus toimii erillisellä ohjelmalla. Minulla oli suunnitelmissa sallia syöttää pääsovellukseen scen-tiedoston, jolloin se suorittaa sen ja tulostaa Flask-sivulle tulokset.

Algoritmit voisivat ehkä palauttaa käytyjen solmujen määrän.

Algoritmien luokkien rakennetta voisi yleisesti parantaa.

scenario_tester-ohjelmalle olisi hyvä tehdä testejä.

### Laajat kielimallit
Kysyin Copilotilta pari kertaa apua docstringien sanoittamisessa.

### Käytetyt lähteet
##### A*
https://en.wikipedia.org/wiki/A*_search_algorithm

##### JPS
http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf

https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search/

##### Oktiilietäisyys
https://doi.org/10.1016/j.cja.2016.04.023