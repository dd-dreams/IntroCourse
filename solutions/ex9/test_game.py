import unittest
import car
import game
from helper import load_json

# Basic
COLORS = ['Y', 'B', 'O', 'W', 'G', 'R']
LEN_BOARD = 7  # python starts from 0
LEN_BOARD1 = 9
file_json = {
    "O": [2, [4, 6], 0],
    "R": [2, [0, 0], 1],
    "Y": [2, [3, 4], 1]
}
CARS = car.Car(COLORS, LEN_BOARD, file_json)
obj = game.Game(CARS, LEN_BOARD, file_json)
CARS_1 = car.Car(COLORS, LEN_BOARD1, file_json)
obj_1 = game.Game(CARS, LEN_BOARD1, file_json)

# testing assignments
generate_coordinates_result = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
    [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7],
    [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7],
    [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7],
    [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
    [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7],
    [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]
]

generate_coordinates_result_1 = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],
    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9],
    [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9],
    [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
    [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
    [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9],
    [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9],
    [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9],
    [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
    [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9],

]


class TestGame(unittest.TestCase):

    def test_generate_coordinates(self):
        result = obj.generate_coordinates()
        self.assertEqual(result, generate_coordinates_result)
        result = obj_1.generate_coordinates()
        self.assertEqual(result, generate_coordinates_result_1)

    def test_get_input(self):
        obj.set_valid_colors(['O', 'R', 'Y'])
        obj.set_return_input("R,R")
        result = obj.return_option()
        self.assertEqual(result, 1, msg="Passed")
        obj.set_return_input("R,D")
        result = obj.return_option()
        self.assertEqual(result, 5, msg="Passed")
        obj.set_return_input("R,L")
        result = obj.return_option()
        self.assertEqual(result, 2, msg="Passed")

    # def test_directions(self):
    #     result = obj.directions('D', -1, -1)
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
