class JumpPointSearch:
    def __init__(self, map: dict):
        self.height = map["height"]
        self.width = map["width"]
        self.grid = map["grid"]

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


    def identify_successor(self, node, start, goal):
        successors = []
        neigbours = self._neighbours(node)
        for n in neigbours:
            #n = self.jump(x, direction(x, n), s, g)
            successors.append(n)
        return successors

    def jump(self, node, direction, start, goal):
        neighbours = self._neighbours(n)
        if n not in neighbours:
            return None
        n = step(node, direction)
        if n == goal:
            return n
        #if n in neighbours so that n' is forced
        #   return n
        if d is diagonal:
            for i in [1,2]:
                if self.jump(n, d(i), start, goal):
                    return n
        return self.jump(n, d, start, goal)