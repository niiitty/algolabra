from services.map_reader import MapReader
from services.a_star import AStar

reader = MapReader("tests/maps/obstacle.map")

grid = reader.convert()
print(AStar(grid).a_star_search((18, 1), (1, 18)))
