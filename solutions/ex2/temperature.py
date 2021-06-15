def is_it_summer_yet(end, day1, day2, day3):
    if (day1 > end and day2 > end) or (day2 > end and day3 > end) or (day1 > end and day3 > end):
        print(True)
    else:
        print(False)


is_it_summer_yet(7, 5, -2, 11)
