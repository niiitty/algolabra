import unittest
from src.services.a_star import AStar


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
        self.a_star = AStar(self.input_dict)

    def test_correct_path_length_open(self):
        start = (0, 0)
        goal = (2, 9)
        result = self.a_star.a_star_search(start, goal)
        self.assertEqual(len(result.path), 10)

    def test_correct_path_length_obstacle(self):
        start = (8, 0)
        goal = (7, 7)
        result = self.a_star.a_star_search(start, goal)
        self.assertEqual(len(result.path), 9)

    def test_no_path_found(self):
        start = (5, 4)
        goal = (4, 7)
        result = self.a_star.a_star_search(start, goal)
        self.assertEqual(result.path, [])
