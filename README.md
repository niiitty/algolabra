# algolabra

## Dokumentaatio
[Määrittelydokumentti](docs/maarittelydokumentti.md)

## Viikkoraportit
[Viikko 1](docs/viikkoraportit/viikko-1.md)

## Käyttöohje

Kloonaa repositorio koneellesi. Lataa projektin riippuvuudet komennolla 
```
poetry install
```

Tämän jälkeen sovellus voidaan käynnistää komennolla
```
poetry run python src/index.py
```

Sovellukseen syötetään map-tiedosto, joita löytyy esimerkiksi `src/tests/maps` tai https://www.movingai.com/benchmarks/grids.html. Lisäksi sovellus ottaa lähtö- ja maalipisteiden koordinaatit muodossa (y, x). Sovellus palauttaa käytetyn ajan sekä lyhyimmän reitin, minkä sen myös piirtää.