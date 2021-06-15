def largest_and_smallest(num, num1, num2):
    if num > num1 and num > num2:
        if num1 < num2:
            return num, num1
        else:
            return num2
    elif num1 > num and num1 > num2:
        if num < num2:
            return num1, num
        else:
            return num1, num2
    else:
        if num < num1:
            return num2, num
        else:
            return num2, num1


largest_and_smallest(17, 1, 6)


def check_largest_and_smallest():
    result = largest_and_smallest(17, 1, 6)
    result1 = largest_and_smallest(1, 17, 6)
    result2 = largest_and_smallest(1, 1, 2)
    result3 = largest_and_smallest(-1, 7, 10)  # Wanted to see what happened when using a negative number
    result4 = largest_and_smallest(10000, 10001, 100000)  # Wanted to test with big numbers
    if result == (17, 1):
        print(True)
    else:
        print(False)
    if result1 == (17, 1):
        print(True)
    else:
        print(False)
    if result2 == (2, 1):
        print(True)
    else:
        print(False)
    if result3 == (10, -1):
        print(True)
    else:
        print(False)
    if result4 == (100000, 10000):
        print(True)
    else:
        print(False)


check_largest_and_smallest()
