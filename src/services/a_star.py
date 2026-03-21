class AStar:
    def __init__(self, map: dict):
        self.height = map["height"]
        self.width = map["width"]
        self.grid = map["grid"]

    def _cost_estimate(self, node, goal):  # Tsebyshev-etäisyys
        x1, y1 = node
        x2, y2 = goal
        return max(abs(x2 - x1), abs(y2 - y1))

    def _reconstruct_path(self, came_from: dict, current):
        total_path = [current]
        while current in came_from.keys():
            current = came_from[current]
            total_path.append(current)

        return total_path[::-1]

    def _neighbours(self, node):
        x, y = node
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]

        neighbours = []

        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y
            if 0 <= nx < self.height and 0 <= ny < self.width:
                if self.grid[nx][ny] == ".":
                    neighbours.append((nx, ny))
        return neighbours

    def a_star_search(self, start: tuple, goal: tuple):
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self._cost_estimate(start, goal)}

        while f_score:
            current = min(f_score, key=f_score.get)
            if current == goal:
                path = self._reconstruct_path(came_from, current)
                return path

            f_score.pop(current)

            neighbouring_nodes = self._neighbours(current)

            for neighbour in neighbouring_nodes:
                if neighbour not in g_score:
                    g_score[neighbour] = float("inf")
                if neighbour not in f_score:
                    f_score[neighbour] = float("inf")

                tentative_g_score = g_score[current]

                if tentative_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = tentative_g_score
                    f_score[neighbour] = tentative_g_score + \
                        self._cost_estimate(neighbour, goal)

        return False
