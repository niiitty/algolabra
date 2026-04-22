import unittest
from src.services.a_star import AStar
from src.utils.grid_tools import GridTools


class TestAStar(unittest.TestCase):
    def setUp(self):
        self.input_dict = {
            'height': 11,
            'width': 10,
            'grid': [
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'T', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'T', 'T', 'T', '.', '.', '.', '.'],
                ['.', '.', '.', 'T', '.', 'T', '.', '.', '.', '.'],
                ['.', '.', '.', 'T', 'T', 'T', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'T', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'T', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', 'T', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]}
        self.a_star = AStar(GridTools(self.input_dict))

    def test_correct_path_length_open(self):
        start = (0, 0)
        goal = (2, 9)
        path = self.a_star.a_star_search(start, goal)[0]
        self.assertEqual(len(path), 10)

    def test_correct_path_length_obstacle(self):
        start = (8, 0)
        goal = (7, 7)
        path = self.a_star.a_star_search(start, goal)[0]
        self.assertEqual(len(path), 8)

    def test_no_path_found(self):
        start = (5, 4)
        goal = (4, 7)
        path = self.a_star.a_star_search(start, goal)[0]
        self.assertEqual(path, False)
