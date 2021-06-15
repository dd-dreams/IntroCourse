import math


def shape_area():
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape == '1':
        radius = math.pi * float(input())**2
        print(radius)
    elif shape == '2':
        a = float(input())
        b = float(input())
        area = a*b
        print(area)
    elif shape == '3':
        side = float(input())
        area = (side**2) * ((3**0.5)/4)
        print(area)
    else:
        print(None)


shape_area()
