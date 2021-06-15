"""
This file represents the cars.
It will see the JSON file, and check which colors-
are valid.
For example: The length of a car can't be bigger then the length of the board.

"""


class Car:
    def __init__(self, colors, len_board, template):
        self.__len_board = len_board
        self.__colors = colors
        self.__template = template

    def exceptions_car(self, config):
        """
        this method will check for exceptions in the car config,
        and return true if valid or false if not.
        :param config: car config: (car length, spot, direction)
        :return: true or false
        """
        good = True
        car_len, spot, direction = config
        # check if the car length bigger then the length of the board
        if car_len >= self.__len_board:
            good = False
        # check if the car coordinates passed the range
        if spot[0] >= self.__len_board - 1 or spot[1] - 1 >= self.__len_board:
            good = False
        # check if the direction provided is good
        if (direction == 0 or direction == 1) and good:
            good = True
        # checks if one of the column position of the car, pass the border
        if spot[1] > self.__len_board and direction == 0 or car_len + spot[1] > self.__len_board and direction == 1:
            good = False
        return good

    def generate_car_config(self, key):
        """
        this method will receive and return the car config
        :param key: color from the json file
        :return: tuple
        """
        car_len = key[0]
        spot = key[1]
        direction = key[2]  # 1 is horizontal, and 0 is for vertical
        return car_len, spot, direction

    def get_car_length(self, color):
        return self.generate_car_config(self.__template[color])[0]

    def get_car_spot(self, color):
        return self.generate_car_config(self.__template[color])[1]

    def get_car_direction(self, color):
        return self.generate_car_config(self.__template[color])[2]

    def check_file_colors(self):
        """
        this will be the "main" method.
        it will check the colors in the template (json file),
        and return the colors that are valid and present in there.
        :return: the valid colors
        """
        found_colors = []
        for color in self.__template:
            car_conf = self.generate_car_config(self.__template[color])
            if color in self.__colors and self.exceptions_car(car_conf):
                found_colors.append(color.upper())
        return found_colors
