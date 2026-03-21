import time

from flask import Flask, render_template, request

from services.map_reader import MapReader
from services.a_star import AStar


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
        sx, sy = int(request.form.get("start_x")), int(
            request.form.get("start_y"))
        gx, gy = int(request.form.get("goal_x")), int(
            request.form.get("goal_y"))

        file_content = map_file.read().decode("utf-8")
        reader = MapReader(file_content)
        map_dict = reader.convert()

        if map_dict["grid"][sx][sy] != "." or map_dict["grid"][gx][gy] != ".":
            raise ValueError(
                "Joko lähtö- tai maalipiste ei ole kuljettavissa.")

        start_time = time.time()
        path = AStar(map_dict).a_star_search((sx, sy), (gx, gy))
        end_time = time.time()
        total_time = end_time - start_time

        if path:
            image = draw_path(map_dict["grid"], path, (sx, sy), (gx, gy))

        return render_template("index.html",
                               path=path,
                               image=image,
                               time=total_time,
                               length=len(path)
                               )
