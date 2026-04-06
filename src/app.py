import time

from flask import Flask, render_template, request

from services.map_reader import MapReader
from services.a_star import AStar
from services.jump_point_search import JumpPointSearch


app = Flask(__name__)


def draw_path(grid, path, start, goal):
    for move in path:
        x, y = move
        grid[x][y] = "/"

    sx, sy = start
    grid[sx][sy] = "S"

    gx, gy = goal
    grid[gx][gy] = "G"

    res = []
    for row in grid:
        res.append("".join(row))

    return res


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        map_file = request.files.get("map-file")
        sx, sy = int(request.form.get("start-x")), int(request.form.get("start-y"))
        gx, gy = int(request.form.get("goal-x")), int(request.form.get("goal-y"))

        reader = MapReader(map_file)
        map_dict = reader.convert()

        if map_dict["grid"][sx][sy] != "." or map_dict["grid"][gx][gy] != ".":
            raise ValueError(
                "Joko lähtö- tai maalipiste ei ole kuljettavissa.")

        start_time = time.time()
        #path = AStar(map_dict).a_star_search((sx, sy), (gx, gy))
        path, res_map = JumpPointSearch(map_dict).jump_point_search((sx, sy), (gx, gy))
        end_time = time.time()
        total_time = end_time - start_time

        if path:
            image = draw_path(res_map, path, (sx, sy), (gx, gy))
        else:
            image = ["".join(row) for row in res_map]
            path = []

        return render_template("index.html",
                               path=path,
                               image=image,
                               time=total_time,
                               length=len(path)
                               )
