from enum import Enum
from math import sqrt


class Directions(Enum):
    VERTICAL = (-1, 0), (1, 0)
    HORIZONTAL = (0, -1), (0, 1)
    DIAGONAL = (1, 1), (1, -1), (-1, 1), (-1, -1)


class AStar:
    def __init__(self, grid):
        self.grid = grid        

    def _reconstruct_path(self, came_from: dict, current):
        total_path = [current]
        path_length = 0
        while current in came_from.keys():
            direction = self.grid.get_direction(current, came_from[current])
            if direction in Directions.DIAGONAL.value:
                path_length += sqrt(2)
            else:
                path_length += 1
            current = came_from[current]
            total_path.append(current)

        return total_path[::-1], round(path_length, 8)

    def a_star_search(self, start: tuple, goal: tuple):
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.grid.cost_estimate(start, goal)}

        while f_score:
            current = min(f_score, key=f_score.get)
            if current == goal:
                path = self._reconstruct_path(came_from, current)
                return path

            f_score.pop(current)

            neighbouring_nodes = self.grid.neighbours(current)

            for neighbour in neighbouring_nodes:
                if neighbour not in g_score:
                    g_score[neighbour] = float("inf")
                if neighbour not in f_score:
                    f_score[neighbour] = float("inf")

                tentative_g_score = g_score[current] + self.grid.cost_estimate(current, neighbour)

                if tentative_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = tentative_g_score
                    f_score[neighbour] = tentative_g_score + \
                        self.grid.cost_estimate(neighbour, goal)

        return False
