# Määrrittelydokumentti
Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)
Dokumentaation kieli: suomi
Harjoitustyön ohjelmointikieli: Python
muita kieliä en hallitse riittävästi.

## Aihe

Harjoitustyön aiheena on toteuttaa kaksi reitinhakualgoritmia sekä vertailla niitä. Ohjelmaan syötetään map-tiedosto ja palauttaa algoritmein tulokset, kuten reitin pituus sekä käytetty aika. Vertailussa karttoina käytetään [Moving AI lab -sivulta](https://www.movingai.com/benchmarks/grids.html) saatuja ei-sokkelomaisia karttoja (esim. Warcraft III).

## Algoritmit
Työssä käytettävät algoritmit sekä niiden ensisijaiset lähteet.

A*: https://en.wikipedia.org/wiki/A*_search_algorithm
JPS: http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf

A*-algoritmin aikavaatimus O(b^d), jossa d on lyhyimmän reitin pituus ja b on haarautumiskerroin. JPS-algoritmin aikavaativuudesta ei löytynyt tietoa.
