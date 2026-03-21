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
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            ]}
        self.a_star = AStar(self.input_dict)

    def test_correct_path_length(self):
        start = (7, 0)
        goal = (4, 7)
        path = self.a_star.a_star_search(start, goal)
        self.assertEqual(len(path), 9)

    def test_no_path_found(self):
        start = (5, 4)
        goal = (4, 7)
        path = self.a_star.a_star_search(start, goal)
        self.assertEqual(path, False)
