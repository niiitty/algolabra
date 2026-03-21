import unittest
from src.services.map_reader import MapReader


class TestMapReader(unittest.TestCase):
    def setUp(self):
        self.reader = MapReader()
        self.reader.read("src/tests/maps/wall.map")
        self.converted = self.reader.convert()

    def test_return_correct_height(self):
        self.assertEqual(11, self.converted["height"])

    def test_return_correct_width(self):
        self.assertEqual(10, self.converted["width"])

    def test_return_correct_grid(self):
        self.assertEqual(self.converted["grid"], [
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
        ])
