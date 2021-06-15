def calculate_mathematical_expression(num, num1, math):
    if math == '+':
        sum1 = int(num + num1)
    elif math == '-':
        sum1 = int(num - num1)
    elif math == '*':
        sum1 = num * num1
    elif math == '/':
        sum1 = num / num1
    else:
        return None
    if num == 0 or num1 == 0:
        return None
    return sum1


def calculate_from_string():
    string = input()
    if '/' in string or '*' in string or '+' in string or '-' in string:
        if '+' in string:
            list1 = string.split('+')
            num3 = float(list1[0]) + float(list1[1])
        elif '-' in string:
            list1 = string.split('-')
            num3 = float(list1[0]) - float(list1[1])
        elif '/' in string:
            list1 = string.split('/')
            if float(list1[1]) == 0:
                return None
            num3 = float(list1[0]) / float(list1[1])
        elif '*' in string:
            list1 = string.split('*')
            num3 = float(list1[0]) * float(list1[1])
        else:
            return print(None)
    else:
        return print(None)
    return num3


