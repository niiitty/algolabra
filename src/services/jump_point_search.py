from enum import Enum
from math import sqrt

from services.grid_tools import GridTools


class Directions(Enum):
    VERTICAL = (-1, 0), (1, 0)
    HORIZONTAL = (0, -1), (0, 1)
    DIAGONAL = (1, 1), (1, -1), (-1, 1), (-1, -1)


class JumpPointSearch:
    def __init__(self, grid):
        self.grid = GridTools(grid)

    def _reconstruct_path(self, came_from: dict, current, start, goal) -> list:
        jump_points = [current]
        while came_from.get(current) is not None:
            current = came_from[current]
            jump_points.append(current)

        total_path = []
        path_length = 0

        for i, jump_point in enumerate(jump_points):
            if jump_points[i] == current:
                x, y = jump_points[i]
                total_path.append((x, y))
                self.grid.drawn_map[start[0]][start[1]] = "S"
                self.grid.drawn_map[goal[0]][goal[1]] = "G"
                return total_path[::-1], path_length

            direction = self.grid.get_direction(
                jump_points[i], jump_points[i + 1])
            x, y = jump_points[i]
            while (x, y) != jump_points[i + 1]:
                total_path.append((x, y))
                x += direction[0]
                y += direction[1]
                if direction in Directions.DIAGONAL.value:
                    path_length += sqrt(2)
                else:
                    path_length += 1
                self.grid.drawn_map[x][y] = "/"

    def _prune(self, parent: tuple, current: tuple) -> list:
        if not parent or parent == current:
            return self.grid.get_neighbours(current)

        cx, cy = current
        dx, dy = self.grid.get_direction(parent, current)

        pruned_neighbours = []

        if dx != 0 and dy != 0:  # vino
            pruned_neighbours.append((cx + dx, cy + dy))
            pruned_neighbours.append((cx + dx, cy))
            pruned_neighbours.append((cx, cy + dy))

            if self.grid.is_blocked(
                    cx - dx, cy) and not self.grid.is_blocked(cx - dx, cy + dy):
                pruned_neighbours.append((cx - dx, cy + dy))
            if self.grid.is_blocked(
                    cx, cy - dy) and not self.grid.is_blocked(cx + dx, cy - dy):
                pruned_neighbours.append((cx + dx, cy - dy))
            return pruned_neighbours

        return self.grid.get_neighbours(current) # pysty ja vaaka

# -+ 0+ ++
# -0 00 +0
# -- 0- +-

    def _has_forced_neighbour(self, node: tuple, direction):
        x, y = node
        if direction in Directions.VERTICAL.value:
            dx = direction[0]
            if (self.grid.is_blocked(x - dx, y - 1) and not self.grid.is_blocked(x, y - 1)
                ) or (self.grid.is_blocked(x - dx, y + 1) and not self.grid.is_blocked(x, y + 1)):
                return True
        elif direction in Directions.HORIZONTAL.value:
            dy = direction[1]
            if (self.grid.is_blocked(x - 1, y - dy) and not self.grid.is_blocked(x - 1, y)
                ) or (self.grid.is_blocked(x + 1, y - dy) and not self.grid.is_blocked(x + 1, y)):
                return True
        elif direction in Directions.DIAGONAL.value:
            dx, dy = direction
            if (self.grid.is_blocked(x - dx, y) and not self.grid.is_blocked(x - dx, y + dy)
                    ) or (self.grid.is_blocked(x, y - dy) and not self.grid.is_blocked(x + dx, y - dy)):
                return True

        return False

    def _jump(self, node: tuple, direction: tuple,
              start: tuple, goal: tuple) -> tuple | None:
        "Rekursiivisesti etsii hyppypisteitä."
        n = node[0] + direction[0], node[1] + direction[1]
        if n not in self.grid.get_neighbours(node):
            return None
        if n == goal:
            self.grid.drawn_map[n[0]][n[1]] = "x"
            return n
        if self._has_forced_neighbour(n, direction):
            self.grid.drawn_map[n[0]][n[1]] = "x"
            return n
        if direction in Directions.DIAGONAL.value:
            # ne kaksi suuntaa johon mennään vinosuunnassa, huom tuplen arvot
            # kertovat nämä
            for d_i in ((direction[0], 0), (0, direction[1])):
                if self._jump(n, d_i, start, goal):
                    self.grid.drawn_map[n[0]][n[1]] = "x"
                    return n
        self.grid.drawn_map[n[0]][n[1]] = ":"
        return self._jump(n, direction, start, goal)

    def jump_point_search(self, start: tuple, goal: tuple):
        came_from = {start: None}
        g_score = {start: 0}
        f_score = {start: self.grid.cost_estimate(start, goal)}
        jump_points = set()
        jump_points.add(start)

        while jump_points:
            current = min(f_score, key=f_score.get)
            if current == goal:
                path, path_length = self._reconstruct_path(
                    came_from, current, start, goal)
                return path, path_length, self.grid.drawn_map

            jump_points.remove(current)
            f_score.pop(current)

            for node in self._prune(came_from[current], current):
                direction = self.grid.get_direction(current, node)
                found = self._jump(current, direction, start, goal)
                if found:
                    jump_points.add(found)
                    if found not in g_score:
                        g_score[found] = float("inf")
                    if found not in f_score:
                        f_score[found] = float("inf")

                    tentative_g_score = g_score[current] + \
                        self.grid.cost_estimate(current, found)

                    if tentative_g_score < g_score[found]:
                        came_from[found] = current
                        g_score[found] = tentative_g_score
                        f_score[found] = tentative_g_score + \
                            self.grid.cost_estimate(found, goal)

        return None, 0, self.grid.drawn_map
