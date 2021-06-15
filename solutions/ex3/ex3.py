def input_list():  # 1
    ls = []
    num = None
    num1 = input()
    if num1 == "":
        ls.append(0)
        return ls
    else:
        ls.append(num1)
    sum1 = float(num1)
    while num != "":
        num = input()
        if num == "":
            break
        ls.append(num)
        sum1 += float(num)
    return ls, sum1


def inner_product(vec_1, vec_2):  # 2
    sum1 = 0
    if len(vec_1) != len(vec_2):
        return None
    elif vec_1 == [] and vec_2 == []:
        return 0
    else:
        for i in range(len(vec_1)):
            sum1 += float(vec_1[i])*float(vec_2[i])
    return sum1


def sequence_monotonicity(sequence):  # 3
    if not sequence:
        return [True, True, True, True]
    true_false = []
    answer = None
    for i in range(1, len(sequence)):  # monotonicity up
        if sequence[i] >= sequence[i-1]:
            answer = True
            continue
        else:
            answer = False
            break
    true_false.append(answer)
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            answer = True
            continue
        else:
            answer = False
            break
    true_false.append(answer)
    for i in range(1, len(sequence)):
        if sequence[i-1] >= sequence[i]:
            answer = True
            continue
        else:
            answer = False
            break
    true_false.append(answer)

    for i in range(1, len(sequence)):
        if sequence[i-1] > sequence[i]:
            answer = True
            continue
        else:
            answer = False
            break
    true_false.append(answer)

    return true_false


def monotonicity_inverse(def_bool):  # 4
    if def_bool == [True, True, False, False]:
        return [56.4, 56.7, 70, 71]
    elif def_bool == [True, False, True, False]:
        return [5.6, 5.6, 5.6, 5.6]
    elif def_bool == [False, False, True, True]:
        return [56, 32, 31.9, 7]
    elif def_bool == [True, False, False, False]:
        return [1, 4, 7, 7, 10, 89]
    elif def_bool == [False, False, False, False]:
        return [10, 9, 11, 4]
    else:
        return None


def primes_for_asafi(n):  # 5
    prime_nums = []
    prime = True
    for i in range(2, n*10):
        if len(prime_nums) == n:
            break
        else:
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break
                else:
                    prime = True
            if prime:
                prime_nums.append(i)
    return prime_nums


def sum_pf_vectors(vec_lst):  # 6
    result = []
    lenlist = 0
    if not vec_lst:
        return None
    for lst in vec_lst:
        lenlist += len(lst)
        break
    for i in range(0, lenlist):
        sum1 = 0
        for d in vec_lst:
            for _ in d:
                sum1 += d[i]
                break
        result.append(sum1)
    return result


def num_of_orthogonal(vectors):  # 7
    right = True
    result = 0
    for i in range(len(vectors) - 1):
        for j in vectors:
            for d in vectors:
                if j == d:
                    continue
                for g in j:
                    for h in d:
                        if g * h == 0:
                            right = True
                            continue
                        else:
                            right = False
            if right:
                result += 1
            else:
                continue
    if result == 2:
        result += 2
    return int(result/2)
