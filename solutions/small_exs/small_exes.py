
class CarDriver:

    def __init__(self, skill, name):
        self.__driver_skill = skill
        self.__name = name

    def get_skill(self):
        return self.__driver_skill

    def get_name(self):
        return self.__name


class Car:

    def __init__(self, speed):
        self.__speed = speed
        self.__driver = None
        self.__cur_dis = 0

    def set_driver(self, driver):
        self.__driver = driver

    def get_driver(self):
        return self.__driver

    def get_driving_speed(self):
        return self.__speed * self.__driver.get_skill()


class RaceTrack:

    def __init__(self, length):
        self.__length = length
        self.__cars = []
        self.__time = 0

    def add_car(self, car):
        self.__cars.append(car)

    def get_length(self):
        return self.__length

    def get_time(self, car):
        self.__time = self.get_length() / car.get_driving_speed()
        return self.__time

    def race(self):
        list_of_dis = []
        for car in self.__cars:
            car.__cur_dis = car.get_driving_speed() * self.get_time(car)
            list_of_dis.append(car.__cur_dis)
        winner_dist = max(list_of_dis)
        for car in self.__cars:
            if car.__cur_dis == winner_dist:
                return car.get_driver().get_name()


# avinoam_driver = CarDriver(100, "avinoam")
# didi_driver = CarDriver(200, "didi")
# avinoam_car = Car(100)
# didi_car = Car(60)
# avinoam_car.set_driver(avinoam_driver)
# didi_car.set_driver(didi_driver)
# our_race_track = RaceTrack(100)
# our_race_track.add_car(avinoam_car)
# our_race_track.add_car(didi_car)
# print(our_race_track.race())


class Shelf:
    def __init__(self):
        self.__piles = []
        self.__item = None

    def place_item_on(self, item, thing):
        self.__item = item
        if thing == self:
            self.__piles.append([])
            return
        for pile in self.__piles:
            if thing == pile[-1]:
                pile.append(item)
                return
        return "There was an error."

    def get_piles(self):
        return self.__piles

    def print_piles(self, piles1):
        for pil in piles1:
            for ite in range(1, len(pil)):
                if ite != 1:
                    print("on\n{}".format(pil[-ite]))
                    continue
                print(pil[-ite])
            print("on\n{}".format(pil[0]))

    def remove(self, item):
        for pile in self.__piles:
            if item == pile[-1]:
                pile.remove(item)
                return


class LUD:
    def __init__(self, len_dict):
        self.__len_dict = len_dict
        self.__diction = {}
        self.__count_keys = 0

    def get_value(self, key):
        return self.__diction.get(key, "Not Found")

    def put(self, key, value):
        if self.__count_keys == self.__len_dict:
            return
        self.__count_keys += 1
        self.__diction.update({key: value})
