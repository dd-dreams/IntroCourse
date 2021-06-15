Hello,

This is a game called "Rush-Hour".
Your goal is to move an **horizontal** car, to the exit point called "E".

# INSTRUCTIONS
When you want to move a car, to a specific direction, 
you input with two chars separated by a comma: Color, Direction

Example: Y,d - Move **_Yellow_** to **_Down_** direction.

### SYMBOLS
--**Car Names**--

Y - Yellow, B - Blue , O - Orange, B - Black, G - Green, R - Red

**--Directions--**

u - Up, d - Down , r - Right, l - left



# CONSTRUCTION
Here I'll explain what I did in most of the methods.
since some methods are a bit confusing, I'll explain them here.

## _board.py_

### `check_if_car_on_car(self, car_to_check, direct, face, colors, current_cars_coordinates):`
This method will check if the car parameter (`car_to_check`) have the same coordinates as another car.
It will generate the car config, and check which directions the car faces to;
if 1 (horizontal): it will add/subtract to the column.
if 0 (vertical): it will add/subtract to the row,
and it will take the car is going to check (not the parameter) coordinates,
and, it will start check if the parameter, and the car he's going to check, have the same coordinates.



## _car.py_

### `deep_copy_dictionary(dictionary):`
What this method does, is to _deep copy_ all the keys and values in the JSON lists,
and copy them to a new dictionary.
I could do: `variable = TEMPLATE`, but then it would do _shallow copy_.
I also didn't want to use additional libraries.


### `generate_coordinates(self):`

This method, just generate the coordinates in a specific range.
It has been used in `board.py` file.

### `check_input(self, direction):`
This method checks the input the user have input, and decides what to do with that.
`option = 1` is move car to the right,
`option = 2` is move car to the left,
`option = 3` is move car upwards,
`option = 4` is move car downwards.

### `update_cars_coordinates(self, color, coordinates):`
This method will update a certain car (_color_), to its new coordinates
after being moved.

### `divied_input(self):`
It will divide the input to by using the comma, to two variables, color, direction.

### `directions(self, color, direct_up_down, direct_right_left):`
This is the longest method.
It will create results by the input, and apply them to the board.

He does that by first generating the car config, and also check if the user tried
to use a direction that is not available to the car, like right direction to a vertical car.
0 stands for vertical, and 1 stands for horizontal. 
Then, it will get the coordinates the car (`coors_of_car`) fills in, then make new coordinates (`new_coors_of_car`)

`direct_up_down` will be used to determine if he wants to go up or down; 1 is down, -1 is up.
The way it makes new coordinates, is first from `spot[0]` (row) it subtracts `direct_up_down`,
and `direct_up_down` can be -1 or 1, which is -1 it adds to the row, going up, and 1 is subtracts
the row, going down. The next argument is the same.

After all of that it will continue to check for exceptions, and if it will pass all of them, 
it will update the board with the new changes, and the new car coordinate.
It will also check if he won or not (if he got to the exit coordinate).
