"""
This file is not part of the exercise.
Y - Yellow, B - Blue , O - Orange, B - Black, G - Green, R - Red

AUTHOR: Yedidya
"""

# --IMPORTING--
from tkinter import *
from game import *


# --ASSIGNING--
WIDTH_FRAME_CARS = 666
HEIGHT_FRAME_CARS = 696
CAR_WIDTH = 100
CAR_HEIGHT = 100
json = 'config.json'
TEMPLATE = load_json(json)
CARS = car.Car(CAR_COLORS, LEN_BOARD, TEMPLATE)
VALID_COLORS = CARS.check_file_colors()
GAME = Game(CARS, LEN_BOARD, TEMPLATE)
GAME.set_valid_colors(VALID_COLORS)
GAME.welcome()


class Gui:
    def __init__(self, image_yellow, image_blue, image_orange, image_black, image_green, image_red, coordinates_cars):
        self.__root = Tk()
        self.__image_yellow = PhotoImage(file=image_yellow)
        self.__image_blue = PhotoImage(file=image_blue)
        # self.__image_orange = PhotoImage(file=image_orange)
        # self.__image_black = PhotoImage(file=image_black)
        # self.__image_green = PhotoImage(file=image_green)
        # self.__image_red = PhotoImage(file=image_red)
        self.__coordinates_cars = coordinates_cars
        self.__exit_button = Button(self.__root, text="Exit", padx=30, pady=20, command=self.__root.quit)
        self.__move_button = Button(self.__root, text="Move", command=self.input_command_button)
        self.__output_box = self.output_box()
        self.__input_command_box = Entry(self.__root, exportselection=0, bd=3)
        self.__frame_cars = Frame(self.__root, width=WIDTH_FRAME_CARS, height=HEIGHT_FRAME_CARS)

    def widgets(self):
        """
        placing and configuring all the widgets in the gui
        :return:
        """
        self.__frame_cars.place(x=40, y=10)
        self.__exit_button.place(x=890, y=30)
        self.__move_button.place(x=905, y=500)
        self.__input_command_box.place(x=853, y=530)
        self.__output_box.config(state=DISABLED)  # making the text box read-only
        self.grid()
        self.cars_widget(self.__image_yellow, 'd')

    def grid(self):
        for line_coor in range(1, LEN_BOARD + 1):
            # was confused with create_line and those stuff, so i just used background
            line_horizontal = Canvas(self.__root, width=4, height=690, bg="black")
            line_vert = Canvas(self.__root, width=653, height=4, bg="black")
            line_horizontal.place(x=(200 * line_coor)//2, y=10)
            line_vert.place(x=50, y=(200 * line_coor)/2)

    def cars_widget(self, car_image, direction):
        car_yellow = Canvas(self.__frame_cars, width=CAR_WIDTH, height=CAR_HEIGHT)
        car_yellow.create_image(20, 50, image=car_image)
        car_yellow1 = Canvas(self.__frame_cars, width=CAR_WIDTH, height=CAR_HEIGHT)
        car_yellow1.create_image(20, 50, image=car_image)
        car_yellow.grid(row=0, column=0)
        car_yellow1.grid(row=1, column=1)

    def input_command_button(self):
        """
        this method will take the same input as if he would type it in a CLI,
        then output it to the output box
        :return:
        """
        self.__output_box.config(state=NORMAL)  # making the text box insertable
        get_input = str(self.__input_command_box.get()).upper()
        if get_input == "":
            output = INPUT_ERROR
        else:
            output = "\n\n" + str(GAME.set_return_input(get_input))
        self.__input_command_box.delete(0, END)  # deleting the contents in the input box
        self.__output_box.insert(END, output)
        self.__output_box.config(state=DISABLED)
        return get_input

    def output_box(self):
        box_frame = Frame(self.__root, height=30, width=20)
        scrollbar = Scrollbar(box_frame, orient=VERTICAL)
        text_box = Text(box_frame, height=20, width=30, bd=4, yscrollcommand=scrollbar.set)
        box_frame.place(x=800, y=130)
        text_box.pack(side=RIGHT)
        scrollbar.pack(side=RIGHT, fill=Y)
        return text_box

    def window(self):
        """
        main window, calling all methods and using them
        :return:
        """
        self.__root.iconphoto(False, PhotoImage(file="images/icon.gif"))
        self.__root.geometry('1100x750')
        # self.__root.resizable(width=False, height=False)
        self.__root.title("Rush-Hour")
        self.widgets()
        self.__root.mainloop()


if __name__ == '__main__':
    gui = Gui("images/yellow_car.png", image_blue="images/blue_car_up.png", image_orange="images/orange_car.png",
              image_black="images/black_car.png", image_green="images/green_car.png", image_red="images/red_car.png",
              coordinates_cars=load_json('config.json'))
    gui.window()
