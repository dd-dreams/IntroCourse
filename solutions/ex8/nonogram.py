"""

This algorithm will solve for you any nonogram game, pretty quick and easily.
"""

CONSTRAINT_LIST = []
count_zeros = 1


def helper_constraint(n, blocks, first_block, curr_block, amount_of_zeros, paint):
    global count_zeros
    # base cases
    if len(paint) > n:
        return
    if curr_block == len(blocks):
        if len(paint) == n:
            CONSTRAINT_LIST.append(paint)
            count_zeros += 1
        return
    # actual recursive
    for pos in range(n):
        helper_constraint(n, blocks, first_block, curr_block + 1, amount_of_zeros=count_zeros,
                          paint=paint + ('1' * curr_block) + ('0' * amount_of_zeros))


def constraint_satisfactions(n, blocks):
    helper_constraint(n, blocks, blocks[0], 0, 1, paint="")


constraint_satisfactions(5, [2, 1])

print(CONSTRAINT_LIST)
