import re
from pathlib import Path


class MapReader:
    def __init__(self, map_file=None):
        if map_file:
            self.read(map_file)

    def read(self, map_file):
        self.map_file = map_file

    def convert(self) -> dict:
        """
        Muuntaa map-tiedoston sanakirjaksi. Sanakirja sisältää kartan pituuden, leveyden sekä 
        kartan matriisina.
        """
        if Path(self.map_file).is_file():
            with open(self.map_file, "r", encoding="utf-8") as f:
                file = f.read().strip()
        else:
            file = str(self.map_file).strip()

        map_dict = {
            "height": self._height(file),
            "width": self._width(file),
            "grid": self._matrix(file)
        }

        return map_dict

    def _matrix(self, file) -> list:
        rows = file.split("\n")
        grid = []
        for row in rows[4:]:
            grid.append(list(row.strip()))
        return grid

    def _height(self, file) -> int:
        text = re.search("height [0-9]+", file)
        value = text.group(0).split()[-1]
        return int(value)

    def _width(self, file) -> int:
        text = re.search("width [0-9]+", file)
        value = text.group(0).split()[-1]
        return int(value)
