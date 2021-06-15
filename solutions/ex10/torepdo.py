

class Torpedo:
    def __init__(self, x=0, y=0, speed_x=0, speed_y=0, angle=0, radius=0):
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__angle = angle
        self.__radius = radius
        self.__life_time = 0

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_speed_x(self, speed_x):
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.__speed_y = speed_y

    def set_angle(self, angle):
        self.__angle = angle

    def add_to_life_time(self):
        self.__life_time += 1

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

    def return_life_time(self):
        return self.__life_time
