"""
This file represent the board.
It will create an empty template, ROWxCOL, and fill it with all the cars-
received from the Car class (car.py).

"""
EXIT = [3, 7]


class Board:
    def __init__(self, board_template, coordinates, len_board, cars):
        self.__board_template = board_template
        self.__square = '_' + ' '
        self.__end_line_char = '*'
        self.__exit_char = "E"
        self.__len_board = len_board  # python starts from 0.
        self.__coordinates = coordinates
        self.__cars = cars
        self.__colors = self.__cars.check_file_colors()
        self.__coordinates_to_edit = []
        self.__final_template = None

    def create_empty_template(self):
        """
        this method will create an empty template-
        by using a 2D list. each list in the list, is a row.
        :return: empty template
        """
        final = []
        for row in range(self.__len_board):
            final.append([])
            for col in range(self.__len_board + 1):
                if col == self.__len_board:
                    final[row].append(self.__end_line_char)
                else:
                    final[row].append(self.__square)
        return final

    def coordinates_from_spot_in_length(self, car_len, spot, face):
        """
        this method will take the starting spot of the car,
        and it will create a new list with coordinates which-
        the car fills in.
        :param car_len: length of car
        :param spot: the starting point of the car
        :param face: vertical or horizontal
        :return: the new coordinate
        """
        # checking if the spot (is out of range)/(passes the border)
        if spot[0] < 0 or spot[1] < 0:
            return None
        if face == 0:
            temp = []
            for row in range(spot[0], spot[0] + car_len):
                temp.append([row, spot[1]])
            return temp
        else:
            index = self.__coordinates.index(spot)
            return self.__coordinates[index:(index + car_len)]

    def check_if_car_on_car(self, car_to_check, direct, face, colors, current_coordinates):  # TODO fix it
        """
        this method will check if two cars have the same coordinates,
        and if they have, that means they are on top of each other.
        :param direct: if he want to go backwards, or forwards, -1 is forward/up, 1 is backwards/down
        :param face: which direction is faces
        :param car_to_check: the car to check if its on top of another car
        :param colors: the valid colors.
        :param current_coordinates: all the coordinates of all car, currently.
        :return: boolean, if they are or not
        """
        for color in colors:
            if color == car_to_check:
                continue
            car_len, spot, direction = self.__cars.generate_car_config(current_coordinates[color])
            check_len, check_spot, check_direction = self.__cars.generate_car_config(current_coordinates[car_to_check])
            coordinates_of_car = self.coordinates_from_spot_in_length(car_len, spot, direction)
            if face == 1:  # to add direct to the column, or row
                coordinates_of_car_to_check = self.coordinates_from_spot_in_length(
                    check_len, [check_spot[0], check_spot[1] + direct], check_direction)
            else:
                coordinates_of_car_to_check = self.coordinates_from_spot_in_length(
                    check_len, [check_spot[0] - direct, check_spot[1]], check_direction)
            for coordinate in coordinates_of_car_to_check:
                if coordinate in coordinates_of_car:
                    return True
        return False

    def json_template(self):
        """
        this method will edit the template as the config-
        says from the JSON file.
        :return: final template
        """
        empty_template = self.create_empty_template()
        for color in self.__colors:
            car_len, spot, direction = self.__cars.generate_car_config(
                self.__board_template[color])
            car_coordinates = self.coordinates_from_spot_in_length(
                car_len, spot, direction)
            for position in self.__coordinates:
                row, col = position
                for car_coordinate in car_coordinates:  # checking if the supposed to be a color there
                    if [row, col] == car_coordinate:
                        empty_template[row][col] = color + ' '
        middle = int(len(empty_template) / 2)
        empty_template[middle][self.__len_board] = self.__exit_char
        self.__final_template = empty_template

    def edit_template(self, color, coordinates_to_edit, car_coordinates):
        self.__coordinates_to_edit.append(coordinates_to_edit)
        template = self.get_template()
        # replacing the coordinates
        for coordinate in car_coordinates:
            row, col = coordinate
            if [row, col] == EXIT:  # if its the exit coordinate
                template[row][col] = self.__exit_char
                continue
            template[row][col] = self.__square
        for coordinate in coordinates_to_edit:
            row, col = coordinate
            template[row][col] = color + ' '
        self.__final_template = template

    def update_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_template(self):
        return self.__final_template

    def __str__(self):
        return "{}".format(self.get_template())
