import math
import glob
from os.path import basename

from services.map_reader import MapReader
from services.a_star import AStar
from services.jump_point_search import JumpPointSearch
from utils.grid_tools import GridTools


class ScenarioTester:
    def read(self, file):
        file_dict = {}
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except BaseException as exc:
            raise FileNotFoundError from exc

        for i, row in enumerate(lines[1:]):
            parts = row.strip().split()

            file_dict[i] = {
                "start_x": int(parts[4]),
                "start_y": int(parts[5]),
                "goal_x": int(parts[6]),
                "goal_y": int(parts[7]),
                "optimal_length": float(parts[8]),
            }

        return file_dict

    def begin_tests(self, scen_file, map_file):
        a_star_correct = 0
        a_star_incorrect = 0

        jps_correct = 0
        jps_incorrect = 0

        file_dict = self.read(scen_file)
        grid = GridTools(MapReader(map_file).convert())

        print("Beginning tests. This may take some time.")

        for scenario in file_dict.values():
            start_x = scenario["start_x"]
            start_y = scenario["start_y"]
            goal_x = scenario["goal_x"]
            goal_y = scenario["goal_y"]
            optimal_length = scenario["optimal_length"]

            start = (start_y, start_x)
            goal = (goal_y, goal_x)

            path, a_star_path_length = AStar(grid).a_star_search(start, goal)

            if math.isclose(a_star_path_length, optimal_length):
                a_star_correct += 1
            else:
                a_star_incorrect += 1

            path, jps_path_length, drawn_map = JumpPointSearch(
                grid).jump_point_search(start, goal)

            if math.isclose(jps_path_length, optimal_length):
                jps_correct += 1
            else:
                jps_incorrect += 1

        print(f"Correct: {a_star_correct}, incorrect: {a_star_incorrect}")
        print(f"Correct: {jps_correct}, incorrect: {jps_incorrect}")


if __name__ == "__main__":
    for map_file in glob.glob("src/tests/maps/*.map"):
        print(basename(map_file).split(".")[0])
    map_name = input("Insert map name: ")
    ScenarioTester().begin_tests(
        f"src/tests/maps/{map_name}.map.scen",
        f"src/tests/maps/{map_name}.map"
    )
