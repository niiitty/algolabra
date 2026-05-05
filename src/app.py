import time

from flask import Flask, render_template, request

from services.map_reader import MapReader
from services.a_star import AStar
from services.jump_point_search import JumpPointSearch


app = Flask(__name__)

saved_map_dict = {}

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", filled={})

    if request.method == "POST":
        map_file = request.files.get("map-file")
        sx, sy = int(request.form.get("start-x")), int(request.form.get("start-y"))
        gx, gy = int(request.form.get("goal-x")), int(request.form.get("goal-y"))

        start = (sy, sx)
        goal = (gy, gx)

        error = None
        filled = {"sx": sx, "sy": sy, "gx": gx, "gy": gy}

        if map_file:
            map_dict = MapReader(map_file).convert()
            global saved_map_dict
            saved_map_dict = map_dict
        elif len(saved_map_dict) != 0:
            map_dict = saved_map_dict
        else:
            error = "Syötä map-tiedosto."
            return render_template("index.html", filled=filled, error=error)

        if map_dict["grid"][sy][sx] != "." or map_dict["grid"][gy][gx] != ".":
            error = "Joko lähtö- tai maalipiste ei ole kuljettavissa."

        if request.form.get("algorithm") == "A*":
            start_time = time.perf_counter()
            path, path_length, resulting_map = AStar(map_dict).a_star_search(start, goal)
        else:
            start_time = time.perf_counter()
            path, path_length, resulting_map = JumpPointSearch(
                map_dict).jump_point_search(start, goal)

        end_time = time.perf_counter()
        total_time = end_time - start_time


        image = []
        for y, row in enumerate(resulting_map):
            rows = []
            for x, node in enumerate(row):
                rows.append({"char": node, "x": x, "y": y})
            image.append(rows)

        return render_template("index.html",
                               error=error,
                               path=path,
                               image=image,
                               time=total_time,
                               length=path_length,
                               filled=filled
                               )
