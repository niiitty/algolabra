import unittest
from src.services.jump_point_search import JumpPointSearch


class TestJumpPointSearch(unittest.TestCase):
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
        self.jps = JumpPointSearch(self.input_dict)

    def test_correct_path_length_open(self):
        start = (0, 0)
        goal = (2, 9)
        path = self.jps.jump_point_search(start, goal)[0]
        self.assertEqual(len(path), 10)

    def test_correct_path_length_obstacle(self):
        start = (8, 0)
        goal = (7, 7)
        path = self.jps.jump_point_search(start, goal)[0]
        self.assertEqual(len(path), 9)

    def test_no_path_found(self):
        start = (5, 4)
        goal = (4, 7)
        path = self.jps.jump_point_search(start, goal)[0]
        self.assertEqual(path, [])
