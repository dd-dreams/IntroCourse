

class Ship:
    def __init__(self, x, y, speed_x, speed_y, angle, radius):
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__angle = angle
        self.__radius = radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_speed_x(self, speed_x):
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.__speed_y = speed_y

    def return_x(self):
        return self.__x

    def return_y(self):
        return self.__y

    def return_speed_x(self):
        return self.__speed_x

    def return_speed_y(self):
        return self.__speed_y

    def return_angle(self):
        return self.__angle

    def return_radius(self):
        return self.__radius
