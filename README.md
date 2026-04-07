# algolabra

## Dokumentaatio
[Määrittelydokumentti](docs/maarittelydokumentti.md)

## Viikkoraportit
[Viikko 1](docs/viikkoraportit/viikko-1.md)

[Viikko 2](docs/viikkoraportit/viikko-2.md)

[Viikko 3](docs/viikkoraportit/viikko-3.md)

[Viikko 4](docs/viikkoraportit/viikko-4.md)

[Viikko 5](docs/viikkoraportit/viikko-5.md)


## Käyttöohje

Kloonaa repositorio koneellesi. Lataa projektin riippuvuudet komennolla 
```
poetry install
```

Tämän jälkeen sovellus voidaan käynnistää komennolla
```
poetry run python src/index.py
```

Sovellukseen syötetään map-tiedosto, joita löytyy esimerkiksi `src/tests/maps` tai https://www.movingai.com/benchmarks/grids.html. Lisäksi sovellus ottaa lähtö- ja maalipisteiden koordinaatit muodossa (x, y). Sovellus palauttaa käytetyn ajan sekä lyhyimmän reitin, minkä sen myös piirtää.
