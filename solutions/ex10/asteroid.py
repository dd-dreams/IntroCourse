

class Asteroid:
    def __init__(self, x, y, speed_x, speed_y, size):
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__size = size
        self.__removed = False

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_speed_x(self, speed_x):
        self.__speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.__speed_y = speed_y

    def return_speed_x(self):
        return self.__speed_x

    def return_x(self):
        return self.__x

    def return_y(self):
        return self.__y

    def return_speed_y(self):
        return self.__speed_y

    def return_size(self):
        return self.__size

    def return_radius(self):
        radius = self.__size * 10 - 5
        return radius

    def return_removed(self):
        return self.__removed

    def has_intersection(self, obj):
        before_root = (obj.return_x() - self.return_x()) ** 2 + (obj.return_y() - self.return_y()) ** 2
        distance = before_root ** 0.5
        if distance <= self.return_radius() + obj.return_radius():
            self.__removed = True
            return True
        return False
