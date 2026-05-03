import time

from flask import Flask, render_template, request

from services.map_reader import MapReader
from services.a_star import AStar
from services.jump_point_search import JumpPointSearch


app = Flask(__name__)

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

        reader = MapReader(map_file)
        map_dict = reader.convert()

        error = None
        filled = {"sx": sx, "sy": sy, "gx": gx, "gy": gy}

        if map_dict["grid"][sy][sx] != "." or map_dict["grid"][gy][gx] != ".":
            error = "Joko lähtö- tai maalipiste ei ole kuljettavissa."
            return render_template("index.html", error=error, filled=filled)

        if request.form.get("algorithm") == "A*":
            start_time = time.time()
            path, path_length = AStar(map_dict).a_star_search(start, goal)
            res_map = map_dict["grid"]
        else:
            start_time = time.time()
            path, path_length, res_map = JumpPointSearch(
                map_dict).jump_point_search(start, goal)

        end_time = time.time()
        total_time = end_time - start_time

        if path:
            image = draw_path(res_map, path, start, goal)
        else:
            image = ["".join(row) for row in res_map]
            path = []

        return render_template("index.html",
                               error=error,
                               path=path,
                               image=image,
                               time=total_time,
                               length=path_length,
                               filled=filled
                               )
