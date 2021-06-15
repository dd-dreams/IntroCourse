"""

Project name: wordsearch
Description: This program will solve a matrix of words.
You choose the desired direction, and the algorithem will check if there is any words-
that in the matrix
Name: fam

"""
import argparse
import os

UP_DIRECTION = 'u'
DOWN_DIRECTION = 'd'
RIGHT_DIRECTION = 'r'
LEFT_DIRECTION = 'l'
DIAGONAL_RIGHT_DIRECTION_UP = 'w'
DIAGONAL_LEFT_DIRECTION_UP = 'x'
DIAGONAL_RIGHT_DIRECTION_DOWN = 'y'
DIAGONAL_LEFT_DIRECTION_DOWN = 'z'
FOUND_WORDS = []
DESCRIPTION = """
This script will find for you words in any size of a matrix.
"""
WORD_LIST_DESCRIPTION = "file with words in it to specify which words are findable"
MATRIX_FILE_DESCRIPTION = "file with the matrix"
DIRECTIONS_DESCRIPTION = "Specify which directions the algorithm should check. " \
                         "UP = u, DOWN = d, LEFT = l, RIGHT = r," \
                         " RIGHT DIAGONAL UP = w, LEFT DIAGONAL UP = x," \
                         " RIGHT DIAGONAL DOWN = y, LEFT DIAGONAL DOWN =z"
OUTPUT_DESCRIPTION = "Which file to output the results"


def read_wordlist(filename):  # this function reads the file with all the words in it
    """

    :param filename: the file with the words to find
    :return: the list with all the words from filename
    """
    try:
        with open(filename, 'r') as WORD_FILE:
            word_list = [line.rstrip() for line in WORD_FILE]  # if i would used readlines() it would add \n so no...
        return word_list
    except FileNotFoundError:
        print("[ERROR] THE WORDLIST FILE SPECIFIED DOESN'T EXIST.")
        exit()


def read_matrix(filename):  # this function reads the matrix file
    """

    :param filename: the matrix file
    :return: returns the two dimensional chars list
    """
    try:
        with open(filename, 'r') as MATRIX_FILE:
            """
            here was a bit of a problem.
            if i would just do readlines and rstrip to remove the '\n' like i did above, it would still-
            not work and sometimes adds '\n'
            so i had to do it the hard way, with the loops.
            """
            matrix_list = [i.strip() for i in MATRIX_FILE.readlines()]
            final_matrix_list = []
            for i in matrix_list:
                chars = []  # all chars for one word
                for j in i:
                    if j == ',':  # so it wont append ',' symbol
                        continue
                    else:
                        chars.append(j)
                final_matrix_list.append(chars)
        return final_matrix_list
    except FileNotFoundError:
        print("[ERROR] THE MATRIX FILE SPECIFIED DOESN'T EXIST.")
        exit()


def check_duplicated_words():  # function to check if there is duplicated words found
    """

    :return: list after it removed duplicated and added to count
    """
    global FOUND_WORDS
    tmp_list = []
    for e in FOUND_WORDS:
        count = FOUND_WORDS.count(e)
        if count > 1:
            tmp_list.append((e, count))
        else:
            tmp_list.append((e, 1))
    for i in tmp_list:
        tmp = i
        if tmp_list.count(i) > 1:
            while i in tmp_list:
                tmp_list.remove(i)
            tmp_list.append(tmp)
    FOUND_WORDS = tmp_list
    return FOUND_WORDS


def check_if_word_in_wordlist(sum_string, wordlist):
    """

    :param sum_string: the final string
    :param wordlist: the wordlist with the findable words
    :return:
    """
    for c in wordlist:
        if c in sum_string:
            FOUND_WORDS.append(c)
        else:
            continue
    return FOUND_WORDS


def lists_from_char(i, matrix_flipped, count_char):
    """

    :param i: the i row
    :param count_char:  the current index of char to make new rows from
    :param matrix_flipped:  the matrix but flipped
    :return: tmp_list
    """
    tmp_list = []  # Cartesian product of a row
    matrix_flipped = matrix_flipped[i:]
    for i in range(len(matrix_flipped)):
        start = matrix_flipped[i][count_char:]  # the start line to check for the other rows
        tmp_list.append(start)
        for c in matrix_flipped[i]:
            index_of_char = matrix_flipped[i].index(c)
            row_from_char = matrix_flipped[i][index_of_char:]
            if len(row_from_char) != len(start) or row_from_char == start:  # so we get only rows from the same char
                # index, or if its equal to start, because i append start in the beginning
                continue
            tmp_list.append(row_from_char)
    for d in range(len(tmp_list)):  # sometimes there is duplicates so i fixed it like this
        try:
            if tmp_list[d] == tmp_list[d + 1]:
                tmp_list.remove(tmp_list[d])
        except IndexError:
            break
    return tmp_list


def up_down_direction(length_of_matrix, matrix, directions, wordlist):
    if directions == 'u':
        matrix_flipped = [matrix[-x] for x in range(1, length_of_matrix)]  # down to top. and did 1 because -0 is 0,
        # and it wont fully flipped
        matrix_flipped.append(matrix[0])
        matrix = matrix_flipped
    else:
        pass
    for i in range(len(matrix[0])):
        sum_string = ""
        for j in range(0, length_of_matrix):
            sum_string += matrix[j][i]
        check_if_word_in_wordlist(sum_string, wordlist)
    return FOUND_WORDS


def right_left_direction(matrix, directions, wordlist):
    for j in matrix:  # this loop will append the i char in every row
        sum_string = ""
        for t in range(len(j)):
            if directions == 'r':
                sum_string += j[t]  # from left to right
            else:
                if t == 0:  # j[-0] is 0, and its not good because we want to from right to left
                    continue
                sum_string += j[-t]  # from right to left
                sum_string += j[0]
        check_if_word_in_wordlist(sum_string, wordlist)
    return FOUND_WORDS


def right_left_diagonal_up_down_direction(matrix, length_of_matrix, wordlist, directions):
    matrix_flipped = []
    if directions == 'w' or directions == 'x':
        matrix_flipped = [matrix[-x] for x in range(1, length_of_matrix)]  # did 1 because -0 is 0, and it wont be
        # fully flipped
        matrix_flipped.append(matrix[0])
        if directions == 'w':
            pass
        else:
            tmp = [x[::-1] for x in matrix_flipped]
            matrix_flipped = tmp
    else:
        if directions == 'y':
            pass
        else:
            tmp = [x[::-1] for x in matrix]
            matrix = tmp
    for i in range(length_of_matrix):  # for every row
        count_char = -1  # the current char, starts with -1
        for _ in range(length_of_matrix):  # for every char
            count_char += 1
            sum_string = ""  # the final "word"
            if directions == 'w' or directions == 'x':
                tmp_list = lists_from_char(i, matrix_flipped, count_char)  # making a new list with new rows from
            else:
                tmp_list = lists_from_char(i, matrix, count_char)  # making a new list with new rows from
            # index of char
            for j in range(length_of_matrix):
                try:
                    sum_string += tmp_list[j][j]
                except IndexError:
                    continue
            check_if_word_in_wordlist(sum_string, wordlist)  # checks if a word has been found
    return FOUND_WORDS


def write_output(results, filename):
    results_file = open(filename, 'w')
    for i in results:
        word = i[0]
        count = i[1]
        results_file.write(word.strip() + ", " + str(count) + '\n')


def fix_output(filename):
    # Sometimes there was duplicates for some reason, so i fixed it here
    with open(filename, 'r') as file:
        fx_list = [i.strip() for i in file.readlines()]
        for i in fx_list:
            count_word = fx_list.count(i)
            if count_word > 1:
                while count_word > 1:
                    count_word -= 1
                    fx_list.remove(i)
    os.remove(filename)
    results_file = open(filename, 'w')
    for i in fx_list:
        results_file.write(i + '\n')
    return


def check_if_direction_is_correct(directions):
    directions_list = ['u', 'd', 'r', 'l', 'w', 'x', 'y', 'z']
    for i in directions:
        if i not in directions_list:
            print("You didn't choose one of the directions!")
            exit()
        else:
            continue


def find_words(wordlist, matrix, directions):
    """

    :param wordlist: file with the all the words
    :param matrix: file with the matrix
    :param directions: directions the user chose
    :return: a list with tuples of the found words in it
    """
    directions = directions.lower()  # so even if he will type in capital
    check_if_direction_is_correct(directions)
    length_of_matrix = len(matrix)  # assuming the rows equally has the same length
    if UP_DIRECTION in directions:
        up_down_direction(length_of_matrix, matrix=matrix, directions=UP_DIRECTION, wordlist=wordlist)
    if DOWN_DIRECTION in directions:
        up_down_direction(length_of_matrix, matrix=matrix, directions=DOWN_DIRECTION, wordlist=wordlist)
    if RIGHT_DIRECTION in directions:
        right_left_direction(matrix=matrix, directions=RIGHT_DIRECTION, wordlist=wordlist)
    if LEFT_DIRECTION in directions:
        right_left_direction(matrix=matrix, directions=LEFT_DIRECTION, wordlist=wordlist)
    if DIAGONAL_RIGHT_DIRECTION_UP in directions:
        right_left_diagonal_up_down_direction(matrix, length_of_matrix, wordlist,
                                              directions=DIAGONAL_RIGHT_DIRECTION_UP)
    if DIAGONAL_LEFT_DIRECTION_UP in directions:
        right_left_diagonal_up_down_direction(matrix, length_of_matrix, wordlist,
                                              directions=DIAGONAL_LEFT_DIRECTION_UP)
    if DIAGONAL_RIGHT_DIRECTION_DOWN in directions:
        right_left_diagonal_up_down_direction(matrix, length_of_matrix, wordlist,
                                              directions=DIAGONAL_RIGHT_DIRECTION_DOWN)
    if DIAGONAL_LEFT_DIRECTION_DOWN in directions:
        right_left_diagonal_up_down_direction(matrix, length_of_matrix, wordlist,
                                              directions=DIAGONAL_LEFT_DIRECTION_DOWN)
    return FOUND_WORDS


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('wordlist', help=WORD_LIST_DESCRIPTION)
    parser.add_argument('matrix_file', help=MATRIX_FILE_DESCRIPTION)
    parser.add_argument('output_file', help=OUTPUT_DESCRIPTION)
    parser.add_argument('directions', help=DIRECTIONS_DESCRIPTION)
    args = parser.parse_args()
    find_words(wordlist=read_wordlist(args.wordlist), matrix=read_matrix(args.matrix_file), directions=args.directions)
    check_duplicated_words()
    write_output(results=FOUND_WORDS, filename=args.output_file)
    fix_output(args.output_file)
    print("Finished :)")
