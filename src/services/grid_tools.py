class GridTools:
    """Luokka yhteisiä työkaluja reitinhakuun.
    """
    def __init__(self, map_dict: dict):
        """Luokan konstruktori, joka alustaa työkalut.

        Args:
            map_dict (dict): Sanakirja, joka sisältää käsiteltävän kartan matriisina sekä sen pituuden ja leveyden. 
        """
        self.height = map_dict["height"]
        self.width = map_dict["width"]
        self.grid = map_dict["grid"]
        self.drawn_map = [row[:] for row in map_dict["grid"]]

    def cost_estimate(self, node: tuple, goal: tuple) -> float:
        """Heurestiikkafunktio. Laskee etäisyyden kahden pisteen välillä. Käytössä oktiilietäisyys.

        Args:
            node (tuple): Lähtöpiste
            goal (tuple): Maalipiste

        Returns:
            float: Oktiilietäisyys kahden pisteen välillä.
        """
        xn, yn = node
        xg, yg = goal

        return (abs(xg - xn) + abs(yg - yn)) + \
            (1.414 - 2) * min(abs(xg - xn), abs(yg - yn))

    def get_neighbours(self, node: tuple) -> list[tuple]:
        """Palauttaa kaikki naapurit, johon solmusta voi liikkua.

        Args:
            node (tuple): Tarkasteltava solmu.

        Returns:
            list[tuple]: Lista solmun laillisia naapureita.
        """
        x, y = node

        cardinal_directions = [
            (0, -1), (1, 0),
            (0, 1), (-1, 0)
        ]

        diagonal_directions = [
            (-1, -1), (1, -1),
            (-1, 1), (1, 1)
        ]

        neighbours = []

        for dx, dy in cardinal_directions:
            nx, ny = x + dx, y + dy
            if not self.is_blocked(nx, ny):
                neighbours.append((nx, ny))

        for dx, dy in diagonal_directions:
            nx, ny = x + dx, y + dy
            if (nx, y) in neighbours and (x, ny) in neighbours:
                if not self.is_blocked(nx, ny):
                    neighbours.append((nx, ny))

        return neighbours

    def in_bounds(self, x, y) -> bool:
        return 0 <= x < self.height and 0 <= y < self.width

    def is_blocked(self, x, y) -> bool:
        """Tarkistaa, onko piste kartan sisällä ja kuljettavissa.

        Args:
            x (int): x-koordinaatti
            y (int): y-koordinaatti

        Returns:
            bool: False, jos solmu on liikuttavissa. True muuten.
        """
        if not self.in_bounds(x, y):
            return True
        return self.grid[x][y] != "."

    def get_direction(self, from_node: tuple, to_node: tuple) -> tuple:
        """Palauttaa kahden solmun normalisoidun suunnan.
        
           | (-1, -1), (0, -1), (1, -1),
           | (-1,  0), (0,  0), (1,  0),
           | (-1,  1), (0,  1), (1,  1)
           
        from_node on käytännössä (0, 0) ja to_node joku sen naapureista.

        Args:
            from_node (tuple): Lähtöpiste.
            to_node (tuple): Kohdepiste.

        Returns:
            tuple: Normalisoitu suunta.
        """
        fx, fy = from_node
        tx, ty = to_node
        dx, dy = tx - fx, ty - fy

        if dy < 0:
            dy = -1
        elif dy > 0:
            dy = 1
        else:
            dy = 0

        if dx < 0:
            dx = -1
        elif dx > 0:
            dx = 1
        else:
            dx = 0

        return dx, dy
