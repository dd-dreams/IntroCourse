"""
AUTHOR: fam
This is a script with some recursion functions.
"""


def helper_print_to_n(maximum, plus):
    if plus <= maximum:
        print(plus)
        helper_print_to_n(maximum, plus + 1)


def print_to_n(n):
    if n == 1:
        print(n)
        return
    helper_print_to_n(n, 1)


def digit_sum(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + digit_sum(n / 10)


def has_divisor_smaller_than(n, i):
    if i == n and i != 1:
        return True
    elif n <= 0 or n == 1:
        return False
    elif n % i == 0:
        if i == 1:
            return has_divisor_smaller_than(n, i + 1)
        return False
    else:
        return has_divisor_smaller_than(n, i + 1)


def is_prime(n):
    if has_divisor_smaller_than(n, 1):
        return True
    return False


def play_hanoi(hanoi, n, src, dest, temp):
    if n == 0:
        return
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def helper_print_sequences(char_list, n, sub_str, repeats):
    if len(sub_str) == n:
        print(sub_str)
        return
    for let in char_list:
        if repeats:
            helper_print_sequences(char_list, n, sub_str + let, True)
        else:
            if let not in sub_str:
                helper_print_sequences(char_list, n, sub_str + let, False)


def print_sequences(char_list, n):
    helper_print_sequences(char_list, n, "", True)


def print_no_repetition_sequences(char_list, n):
    """

    :param char_list: the list of chars
    :param n: how long the possible combinations of chars can be
    :return:
    """
    helper_print_sequences(char_list, n, "", False)


def _parentheses(final, open_par, close, n, parentheses_list):
    """

    :param final: the string to add parentheses
    :param open_par: open parent
    :param close: close parent
    :param n: how many parentheses can there be
    :return: its a recursive function
    """
    if final.count(')') == n:  # every close parentheses has a open parentheses
        parentheses_list.append(final)
        pass
    else:
        if open_par < n:
            _parentheses(final + '(', open_par + 1, close, n, parentheses_list)
        if close < open_par:
            _parentheses(final + ')', open_par, close + 1, n, parentheses_list)


def parentheses(n):
    parentheses_list = []
    _parentheses("", 0, 0, n, parentheses_list)
    return parentheses_list


def flood_fill(image, start):
    """

    :param image: the image to check
    :param start: what index to start from
    :return: nothing
    """
    line = start[0]  # index of line
    column = start[1]  # index of column
    if image[line][column] == '.':
        image[line][column] = '*'  # default
        if image[line][column + 1] == '.':  # next item in the current line
            flood_fill(image, (line, column + 1))
        if image[line][column - 1] == '.':  # previous item in the current line
            flood_fill(image, (line, column - 1))
        if line > 0:
            if image[line - 1][column] == '.':  # above line
                flood_fill(image, (line - 1, column))
            if image[line + 1][column] == '.':  # bottom line
                flood_fill(image, (line + 1, column))
