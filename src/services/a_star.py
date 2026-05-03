import heapq

from enum import Enum
from math import sqrt

from services.grid_tools import GridTools

class Directions(Enum):
    VERTICAL = (-1, 0), (1, 0)
    HORIZONTAL = (0, -1), (0, 1)
    DIAGONAL = (1, 1), (1, -1), (-1, 1), (-1, -1)


class AStar:
    def __init__(self, grid):
        self.grid = GridTools(grid)

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

        return total_path[::-1], path_length

    def a_star_search(self, start: tuple, goal: tuple):
        came_from = {}
        open_set = []
        g_score = {start: 0}
        f_score = {start: self.grid.cost_estimate(start, goal)}

        heapq.heappush(open_set, (f_score[start], start))

        visited = set()
        while open_set:
            current = heapq.heappop(open_set)[1] # valitaan pelkkä node
            if current in visited:
                continue
            if current == goal:
                path, path_length = self._reconstruct_path(came_from, current)
                return path, path_length, self.grid.drawn_map
            visited.add(current)
            self.grid.drawn_map[current[0]][current[1]] = ":"
            neighbouring_nodes = self.grid.get_neighbours(current)

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
                    if neighbour not in open_set:
                        heapq.heappush(open_set, (f_score[neighbour], neighbour))

        return [], 0, self.grid.drawn_map
