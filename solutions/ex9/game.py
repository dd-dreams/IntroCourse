from helper import load_json
import board
import car
from sys import argv

# ----Basic assignments---- #
CAR_COLORS = ['Y', 'B', 'O', 'B', 'G', 'R']
LEN_BOARD = 7
RIGHT_DIRECTION = 'R'
LEFT_DIRECTION = 'L'
UP_DIRECTION = 'U'
DOWN_DIRECTION = 'D'
HORIZONTAL_CAR = 1
VERTICAL_CAR = 0
EXIT_SPOT = [3, 6]
ERROR_SIGN = "ERROR"

# ----Messages---- #
WELCOME_MESSAGE = "Welcome! This is a Rush-Hour game!\n"
INSTRUCTIONS = """
Your goal is to get to the exit point (E), with whatever car you want,
as long the car is horizontal.
Enjoy!!!!
"""
INPUT_MESSAGE = "Please input the car you want to move, and to which location (color, direction): "
INPUT_ERROR = "\nYou have input a wrong input. Please try again."
CANT_USE_DIRECTION = "\nYou can't use that direction. Try again."
PASS_BORDER_ERROR = "\nThe direction you chose for the car, passes the border. Try again."
WON_MSG = "\nYou won! Good game :)\n"
SUCCESSFULLY_MOVED = "You successfully moved the car."


def deep_copy_dictionary(dictionary):
    return {key: value for key, value in dictionary.items()}


def welcome_message():
    print(WELCOME_MESSAGE)
    print(INSTRUCTIONS)


def check_win(coordinates):
    for coordinate in coordinates:
        if coordinate == EXIT_SPOT:  # TODO make it for any length of board
            print(WON_MSG)
            return True
    return False


def unusable_direction(move_direction, horizontal_vert):
    """
    this method will check what if the user want to use an usable direction-
    for a specific color. for example: down direction for an horizontal car.
    :param move_direction: the direction the player want to move to
    :param horizontal_vert: where the car faces to, horizontal or vertical
    :return: True there is no issue, or False there is
    """
    if (move_direction == RIGHT_DIRECTION or move_direction == LEFT_DIRECTION) and horizontal_vert == VERTICAL_CAR:
        return False
    elif (move_direction == UP_DIRECTION or move_direction == DOWN_DIRECTION) and horizontal_vert == HORIZONTAL_CAR:
        return False
    else:
        return True


class Game:
    def __init__(self, cars, length, template):
        self.__len_board = length
        self.__board = board.Board(template, self.generate_coordinates(), self.__len_board,
                                   cars)
        self.__square = '_'
        self.__end_line_char = '*'
        self.__cars = cars
        self.__valid_colors = None
        self.__template = self.__board.json_template()
        self.__cars_coordinates = deep_copy_dictionary(template)
        self.__input = None
        self.__option = 5
        self.__directions = ['U', 'D', 'R', 'L']

    def print_board(self):
        """
        just prints the board
        :return:
        """
        temp_board = self.__board.get_template()
        print()
        for row in temp_board:
            final = ""
            for col in row:
                final += col
            print(final)

    def welcome(self):
        welcome_message()
        self.print_board()

    def generate_coordinates(self):
        """
        this method will generate all the coordinates-
        available in a specific range.
        :return: generated coordinates
        """
        coordinates = []
        for row in range(self.__len_board + 1):
            for col in range(self.__len_board + 1):
                coordinates.append([row, col])
        return coordinates

    def update_cars_coordinates(self, color, coordinates):
        """
        this method will update the current spot of the car that just moved.
        :param color: which color to update his coordinates
        :param coordinates: with what coordinates to update
        :return:
        """
        car_len, spot, direction = self.__cars.generate_car_config(
            self.__cars_coordinates[color])
        self.__cars_coordinates[color] = [car_len, coordinates[0], direction]
        return self.__cars_coordinates

    def divide_input(self):
        """
        this method divides the input between the color, and direction
        :return: color, direction
        """
        if ',' not in self.__input:
            return ERROR_SIGN, ERROR_SIGN
        color_input, direction_input = self.__input.split(',')
        return color_input, direction_input

    def directions(self, color, direct_up_down, direct_right_left):
        """

        :param color: the car to move
        :param direct_up_down: decides whether the car is moving up or down (look check_if_car_on_car API)
        :param direct_right_left: decides whether the car is moving right or left         ^
        :return: if the game end or not
        """
        if (direct_up_down == -1 or 1 or 0) or (direct_right_left == -1 or 1 or 0):
            pass
        else:
            return False
        car_len, spot, direction = self.__cars.generate_car_config(self.__cars_coordinates[color])
        coors_of_car = self.__board.coordinates_from_spot_in_length(
            car_len, spot, direction)
        # making new coordinates of the car according to the input
        new_coors_of_car = self.__board.coordinates_from_spot_in_length(car_len,
                                                                        [spot[0] - direct_up_down, spot[1] +
                                                                         direct_right_left], direction)
        # checking if the car passes the border
        if new_coors_of_car is None:
            return PASS_BORDER_ERROR
        if direct_right_left == 1 or direct_right_left == -1:
            forward_back = direct_right_left
        else:
            forward_back = direct_up_down
        if self.__board.check_if_car_on_car(color, forward_back, direction, self.__valid_colors,
                                            self.__cars_coordinates):
            return CANT_USE_DIRECTION
        if not self.__cars.exceptions_car((car_len, new_coors_of_car[0], direction)):
            return PASS_BORDER_ERROR
        # editing the template according to the coordinates
        self.__board.edit_template(color, new_coors_of_car, coors_of_car)
        self.__template = self.__board.get_template()
        self.update_cars_coordinates(color, new_coors_of_car)
        if direction == HORIZONTAL_CAR and check_win(new_coors_of_car):  # check if won
            return True
        return False

    def check_input(self, color, direction):
        """
        this method will check the input.
        1 is for "move car to the right", 2 is for "move car to the left",
        3 is for "move car up", 4 is for "move car down", 5 if for "error", 6 is for "end the game",
        :return: an int which will decide what to do
        """
        self.__option = 5
        if (color, direction) == (ERROR_SIGN, ERROR_SIGN):
            return self.__option
        if self.__input is not None:
            if unusable_direction(direction, self.__cars.get_car_direction(self.__input[0])):
                if len(self.__input) == 3 and self.__input[0].isalpha() and self.__input[1] == ',' \
                        and self.__input[2].isalpha():
                    if direction == RIGHT_DIRECTION:
                        self.__option = 1
                    elif direction == LEFT_DIRECTION:
                        self.__option = 2
                    elif direction == UP_DIRECTION:
                        self.__option = 3
                    elif direction == DOWN_DIRECTION:
                        self.__option = 4
            else:
                self.__option = 5
        return self.__option

    def handle_input(self):
        """
        this method will take and input, and handle it.
        it will check the color and direction, and decide what to do.
        :return:
        """
        end = False  # if the game end or not
        # checking if he wanted to end the game
        if self.__input == '!':  # checking if he wanted to end the game
            return True
        color_input, direction_input = self.divide_input()
        self.check_input(color_input, direction_input)
        if self.__option != 5:
            if self.__option == 1:  # right direction
                end = self.directions(color_input, 0, 1)
            elif self.__option == 2:  # left direction
                end = self.directions(color_input, 0, -1)
            elif self.__option == 3:
                end = self.directions(color_input, 1, 0)
            elif self.__option == 4:
                end = self.directions(color_input, -1, 0)
        else:
            return INPUT_ERROR
        self.print_board()
        if end:
            return end
        return SUCCESSFULLY_MOVED

    def get_car_start_coordinate(self, color):
        return self.__cars.get_car_direction(color)

    def set_return_input(self, command):
        self.__input = command
        done = self.handle_input()
        return done

    def return_input(self):
        return self.__input

    def return_option(self):
        return self.__option

    def set_valid_colors(self, valid_colors):
        self.__valid_colors = valid_colors
        return self.__valid_colors


if __name__ == '__main__':
    try:
        json = argv[1]
        TEMPLATE = load_json(json)
        if not TEMPLATE:
            print("JSON file not found.")
        else:
            CARS = car.Car(CAR_COLORS, LEN_BOARD, TEMPLATE)
            VALID_COLORS = CARS.check_file_colors()
            game = Game(CARS, LEN_BOARD, TEMPLATE)
            game.set_valid_colors(VALID_COLORS)
            game.welcome()
            while True:
                _input = input(INPUT_MESSAGE).upper()
                end_game = game.set_return_input(_input)
                if end_game is True:
                    break
                elif end_game is not None:
                    print(end_game)
    except IndexError:
        print("Input config file name.")
