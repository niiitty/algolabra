class GridTools:
    def __init__(self, map_dict: dict):
        self.height = map_dict["height"]
        self.width = map_dict["width"]
        self.grid = map_dict["grid"]
        self.drawn_map = [row[:] for row in map_dict["grid"]]

    def cost_estimate(self, node, goal):
        "Heurestiikkafunktio. Oktiilietäisyys."
        xn, yn = node
        xg, yg = goal

        return (abs(xg - xn) + abs(yg - yn)) + \
            (1.414 - 2) * min(abs(xg - xn), abs(yg - yn))

    def get_neighbours(self, node):
        "Palauttaa kaikki naapurit, joihin voi siirtyä."
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
        if not self.in_bounds(x, y):
            return True
        return self.grid[x][y] != "."

    def get_direction(self, from_node: tuple, to_node: tuple) -> tuple:
        "Palauttaa normalisoidun suunnan."
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
