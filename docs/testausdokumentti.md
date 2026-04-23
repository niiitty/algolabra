# Testausdokumentti

<!---
Yksikkötestauksen kattavuusraportti.
Mitä on testattu, miten tämä tehtiin?
Minkälaisilla syötteillä testaus tehtiin?
Miten testit voidaan toistaa?
--->

## Testien ajaminen
Yksikkötestit voidaan ajaa projektin juurihakemistosta komennolla
```
poetry run python -m pytest
```

scen-tiedostoilla testaaminen tapahtuu erillisellä scenario reader -ohjelmalla, joka ajetaa komennolla
```
poetry run python src/scenario_reader.py
```
Ohjelma ensin luettelee `src/tests/maps/`-polussa sijaitsevat map-tiedostot. Valmiiksi lisätyillä kartoilla on vastaava scen-tiedosto myös kansiossa. Kun käyttäjä on valinnut kartan, kaikki sen skenaariot käydään läpi. Ohjelma vertaa molemmilla algoritmeilla saadun polun pituutta odotettuun optimipituuteen ja tarkistaa, että algoritmien tuottamat pituudet ovat yhtä suuret.

<!---
Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)
--->