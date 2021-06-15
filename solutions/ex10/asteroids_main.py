from screen import Screen
import sys

# my imports
from random import randint
from math import cos, sin, radians
from ship import *
from asteroid import *
from torepdo import *

DEFAULT_ASTEROIDS_NUM = 5

# my assignments
ASTEROIDS_SIZE = 3
TORPEDO_RADIUS = 4
TORPEDO_LIFE_TIME = 200
RETRIES_AMOUNT = 3
DEFAULT_SHIP_HEADING = 0.0
HIT_ASTEROID_TITLE = "You got hit!"
HIT_ASTEROID = "You got hit by an asteroid bruh, careful!"
LOSE_TITLE = "You lost BRUHHHHHHHHH!"
LOSE_MSG = "You lost. Next time :) (bruh)"
WON_TITLE = "You won!"
WON_MSG = "BRUHHH you won whoooo!"


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        # my assignments
        print("Starting...")
        self.__asteroids_amount = asteroids_amount
        self.__asteroids_objects = []
        self.__torpedo_objects = []
        self.__is_start = True
        self.__avg_x = self.__screen_max_x - self.__screen_min_x
        self.__avg_y = self.__screen_max_y - self.__screen_min_y
        self.__ship_angle = 0
        self.__ship = Ship(x=0, y=0, speed_x=0, speed_y=0, angle=0, radius=1)
        self.__lives = 3
        self.__is_torpedo_launched = False
        self.__score = RETRIES_AMOUNT
        self.spawn_asteroids()

    # ----GENERAL METHODS----

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def check_if_keys_pressed(self):
        """
        this method will check if any of the specific keys have been pressed
        :return:
        """

        self.check_win()
        if self.__screen.is_up_pressed() == 1:
            self.speed_up()
        elif self.__screen.is_right_pressed() == 1:
            self.change_angle(True, False)
        elif self.__screen.is_left_pressed() == 1:
            self.change_angle(False, True)
        elif self.__screen.is_space_pressed() == 1:
            self.spawn_torpedo()
        elif self.__screen.should_end():
            print("[!] Player exited")
            self.__screen.end_game()
            sys.exit(0)

    def check_win(self):
        """
        this method will check if the player has won
        :return: false if he didn't win
        """

        if len(self.__asteroids_objects) == 0:
            self.__screen.show_message(WON_TITLE, WON_MSG)
            self.__screen.end_game()
            print("Player won")
            sys.exit(0)
        elif self.__lives == 0:
            self.__screen.show_message(LOSE_TITLE, LOSE_MSG)
            self.__screen.end_game()
            print("Player lost")
            sys.exit(0)
        return False

    def set_score(self, asteroid_obj):
        """
        this method will update the score according to the asteroid size
        :param asteroid_obj: according to size of asteroid obj
        :return:
        """

        if asteroid_obj.return_size() == 3:
            self.__score += 20
        elif asteroid_obj.return_size() == 2:
            self.__score += 50
        else:  # asteroid with 1 size
            self.__score += 100
        self.__screen.set_score(self.__score)  # updating

    def _game_loop(self):
        self.check_win()
        self.spawn_ship()
        self.move_asteroids()
        self.check_if_keys_pressed()
        self.move_ship()
        if len(self.__torpedo_objects) > 0:  # to check the torpedoes status and move him
            for torpedo in self.__torpedo_objects:
                torpedo.add_to_life_time()
                self.check_torpedo_time(torpedo)
            self.move_torpedo()

    # ----SHIP METHODS----

    def change_angle(self, right_bool, left_bool):
        """
        this method will change the angle of the ship,
        according to the player keystrokes
        :param right_bool: true if he wanted to move right
        :type right_bool: bool
        :param left_bool: true if he wanted to move left
        :type left_bool: bool
        :return: angle of ship
        """

        if right_bool:
            self.__ship_angle -= 7
        elif left_bool:
            self.__ship_angle += 7
        return self.__ship_angle

    def spawn_ship(self):
        """
        this method will spawn the ship, and check if-
        the ship already was spawned to prevent spawning infinitely
        :return:
        """
        self.check_win()
        if not self.__is_start:
            return
        print("Spawning ship")
        random_x = randint(self.__screen_min_x, self.__screen_max_x)
        random_y = randint(self.__screen_min_y, self.__screen_max_y)
        self.__ship.set_x(random_x)
        self.__ship.set_y(random_y)
        self.__screen.draw_ship(self.__ship.return_x(), self.__ship.return_y(), DEFAULT_SHIP_HEADING)
        self.__is_start = False

    def speed_up(self):
        """
        this method will speed up the ship speed if requested
        :return:
        """

        print("Speeding up!")
        radians_angle = radians(self.__ship_angle)
        newspeed_x = self.__ship.return_speed_x() + cos(radians_angle)
        newspeed_y = self.__ship.return_speed_y() + sin(radians_angle)
        self.__ship.set_speed_x(newspeed_x)
        self.__ship.set_speed_y(newspeed_y)

    def move_ship(self):
        """
        this method will change a object location in X,Y axis
        it firsts appends for asteroids_amount times and making new spots,
        the first [new] spot is always the ship spot, and the other ones is the asteroids new spots
        :return: new spot of object in Y axis
        """

        self.check_win()
        if self.__is_start:  # check if its the start of the game, because if yes there will be division by 0
            return
        newspot_x = self.__screen_min_x + (
                self.__ship.return_x() + self.__ship.return_speed_x() - self.__screen_min_x) % self.__avg_x
        newspot_y = self.__screen_min_y + (
                self.__ship.return_y() + self.__ship.return_speed_y() - self.__screen_min_y) % self.__avg_y
        self.__screen.draw_ship(newspot_x, newspot_y, self.__ship_angle)
        self.__ship.set_x(newspot_x)
        self.__ship.set_y(newspot_y)

    # ----ASTEROIDS METHODS----

    @staticmethod
    def set_asteroid_speed_spot(obj, random_x, random_y, random_speed_x, random_speed_y):
        """
        this method will initialize the asteroid starting spot and speed
        :param obj: asteroid object
        :param random_x: the randomized x spot
        :param random_y: the randomized y spot
        :param random_speed_x: the randomized speed on the X axis
        :param random_speed_y: the randomized speed on the Y axis
        :return:
        """

        obj.set_x(random_x)
        obj.set_y(random_y)
        obj.set_speed_x(random_speed_x)
        obj.set_speed_y(random_speed_y)

    def spawn_asteroids(self):
        """
        this method will spawn on the start of the game the asteroids
        :return:
        """

        if not self.__is_start:  # checking if its the start of the game
            return
        for asteroid in range(self.__asteroids_amount):
            random_x = randint(self.__screen_min_x, self.__screen_max_x)
            random_y = randint(self.__screen_min_y, self.__screen_max_y)
            random_speed_x = randint(1, 4)
            random_speed_y = randint(1, 4)
            asteroid_obj = Asteroid(random_x, random_y, random_speed_x, random_speed_y, ASTEROIDS_SIZE)
            self.set_asteroid_speed_spot(asteroid_obj, random_x, random_y, random_speed_x, random_speed_y)
            self.__asteroids_objects.append(asteroid_obj)
            self.__screen.register_asteroid(asteroid_obj, ASTEROIDS_SIZE)
            self.__screen.draw_asteroid(asteroid_obj, asteroid_obj.return_x(), asteroid_obj.return_y())
        print("Spawned asteroids")

    @staticmethod
    def new_asteroid_speed(torpedospeed_x, torpedospeed_y, ast_obj):
        """
        this method will generate the new speed of the splitted asteroids
        :param torpedospeed_x: the torpedo current speed on the X axis
        :param torpedospeed_y: the torpedo current speed on the Y axis
        :param ast_obj: the asteroid object
        :return: the new coordinates
        """

        newasteroidspeed_x = (torpedospeed_x + ast_obj.return_speed_x()) / (ast_obj.return_speed_x() ** 2 +
                                                                            ast_obj.return_speed_y() ** 2) ** 0.5
        newasteroidspeed_y = -(torpedospeed_y + ast_obj.return_speed_y()) / (ast_obj.return_speed_x() ** 2 +
                                                                             ast_obj.return_speed_y() ** 2) ** 0.5
        return newasteroidspeed_x, newasteroidspeed_y

    def split_asteroid(self, ast_obj, tor_obj):
        """
        this method will split the asteroids to two smaller asteroids or make him disappear
        :param ast_obj: the asteroid object which got hit
        :param tor_obj:
        :return:
        """

        self.check_win()
        ast_size = ast_obj.return_size()
        self.__screen.unregister_asteroid(ast_obj)
        self.__asteroids_objects.remove(ast_obj)
        if ast_size == 3 or ast_size == 2:
            size = 2 if ast_size == 3 else 1  # if the radius of an asteroid is 3, or 2
            asteroid_new_speed_x, asteroid_new_speed_y = \
                self.new_asteroid_speed(tor_obj.return_speed_x(), tor_obj.return_speed_y(), ast_obj)
            for i in range(2):
                # splitting to two different directions
                if i == 1:
                    asteroid = Asteroid(
                        ast_obj.return_x(), ast_obj.return_y(), -asteroid_new_speed_x, -asteroid_new_speed_y, size)
                else:
                    asteroid = Asteroid(
                        ast_obj.return_x(), ast_obj.return_y(), asteroid_new_speed_x, asteroid_new_speed_y, size)
                self.__screen.register_asteroid(asteroid, size)
                self.__asteroids_objects.append(asteroid)

    def check_hit(self, obj):
        """
        this method will check if an object (ship, torpedo) got hit,
        and if it does, it will remove the which asteroid got hit
        :param obj: asteroid object
        :return: true if the was an hit and false if wasn't
        """

        self.check_win()
        hit_or_not = False
        if not obj.return_removed():
            if obj.has_intersection(self.__ship):  # checking if the ship has hit an asteroid object
                print("[!] Ship hit")
                self.__screen.show_message(HIT_ASTEROID_TITLE, HIT_ASTEROID)
                self.__screen.remove_life()
                self.__screen.unregister_asteroid(obj)
                self.__asteroids_objects.remove(obj)  # we unregistered the asteroid,we also need to remove it from list
                self.__lives -= 1  # the ship was hit
                hit_or_not = True
            for torpedo in self.__torpedo_objects:
                if obj.has_intersection(torpedo):  # checking if a torpedo hit an asteroid object
                    print("[!] Torpedo hit")
                    if self.__is_torpedo_launched:
                        self.split_asteroid(obj, torpedo)
                        print("[!] New asteroids spawned")
                        self.__torpedo_objects.remove(torpedo)
                        self.__screen.unregister_torpedo(torpedo)
                        if len(self.__torpedo_objects) == 0:
                            self.__is_torpedo_launched = False
                        self.set_score(obj)
                    hit_or_not = True
        return hit_or_not

    def move_asteroids(self):
        """
        this method will move all asteroids objects, in the same angle
        :return:
        """

        self.check_win()
        for asteroid_obj in self.__asteroids_objects:
            newspot_x = self.__screen_min_x + (
                    asteroid_obj.return_x() + asteroid_obj.return_speed_x() - self.__screen_min_x) % self.__avg_x
            newspot_y = self.__screen_min_y + (
                    asteroid_obj.return_y() + asteroid_obj.return_speed_y() - self.__screen_min_y) % self.__avg_y
            self.__screen.draw_asteroid(asteroid_obj, newspot_x, newspot_y)
            asteroid_obj.set_x(newspot_x)
            asteroid_obj.set_y(newspot_y)
            self.check_hit(asteroid_obj)

    # ----TORPEDO METHODS----

    def check_torpedo_time(self, tor_obi):
        """
        this method will check the torpedo time
        :param tor_obi: torpedo object
        :return: if the the torpedo object was removed
        """

        if tor_obi.return_life_time() >= 200:
            self.__torpedo_objects.remove(tor_obi)
            self.__screen.unregister_torpedo(tor_obi)
            return True
        return False

    def spawn_torpedo(self):
        """
        this method will spawn a torpedo after space key has been pressed
        :return: true if a torpedo was spawned
        """

        self.check_win()
        if len(self.__torpedo_objects) >= 10:
            print("[!] Couldn't spawn Torpedo, there is already 10 of them.")
            return False
        self.__is_torpedo_launched = True
        torpedospeed_x = self.__ship.return_speed_x() + 2 * cos(radians(self.__ship_angle))
        torpedospeed_y = self.__ship.return_speed_y() + 2 * sin(radians(self.__ship_angle))
        torpedo = Torpedo(TORPEDO_RADIUS)
        torpedo.set_speed_x(torpedospeed_x)
        torpedo.set_speed_y(torpedospeed_y)
        torpedo.set_x(self.__ship.return_x())
        torpedo.set_y(self.__ship.return_y())
        torpedo.set_angle(self.__ship_angle)
        self.__screen.register_torpedo(torpedo)
        self.__torpedo_objects.append(torpedo)
        print("[!] Spawned Torpedo")
        return True

    def move_torpedo(self):
        """
        this method will move each torpedo and remove him if-
        his life time finished
        :return:
        """

        self.check_win()
        if not self.__is_torpedo_launched:
            return
        for torpedo in self.__torpedo_objects:
            newspot_x = self.__screen_min_x + (
                    torpedo.return_x() + torpedo.return_speed_x() - self.__screen_min_x) % self.__avg_x
            newspot_y = self.__screen_min_y + (
                    torpedo.return_y() + torpedo.return_speed_y() - self.__screen_min_y) % self.__avg_y
            self.__screen.draw_torpedo(torpedo, newspot_x, newspot_y, self.__ship_angle)
            torpedo.set_x(newspot_x)
            torpedo.set_y(newspot_y)


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
