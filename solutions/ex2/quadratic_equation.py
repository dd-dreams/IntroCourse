def quadratic_equation(a, b, c):
    root = (b ** 2 - 4 * a * c) ** 0.5
    fir_solution = (b*-1 - root) / 2*a
    sec_solution = (b*-1 + root) / 2*a
    if 'j' in str(fir_solution) and 'j' in str(sec_solution):
        return None
    elif fir_solution == sec_solution:
        return fir_solution
    elif (a*(fir_solution**2) + (b*fir_solution) + c) == 0:
        if (a*sec_solution**2 + (b*sec_solution) + c) == 0:
            return fir_solution, sec_solution
        else:
            return fir_solution, None
    elif (a*(sec_solution**2) + (b*sec_solution) + c) == 0:
        if 'j' in str(fir_solution):
            return sec_solution, None
        else:
            pass
    else:
        pass


quadratic_equation(1, -8, 34.5)


def quadratic_equation_input():
    nums = input("Insert coefficients a,b, and c: ").split(' ')
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    root = (b ** 2 - 4 * a * c) ** 0.5
    fir_solution = (b*-1 - root) / 2*a
    sec_solution = (b*-1 + root) / 2*a
    if a == 0:
        print("The parameter 'a' may not equal to 0")
    elif 'j' in str(fir_solution) and 'j' in str(sec_solution):
        print("The equation has no solutions")
    elif fir_solution == sec_solution:
        print("The equation has 1 solution:", fir_solution)
    elif (a*(fir_solution**2) + (b*fir_solution) + c) == 0:
        if (a*sec_solution**2 + (b*sec_solution) + c) == 0:
            print("The equation has 2 solutions:", fir_solution, "and", sec_solution)
        else:
            print("The equation has 1 solution:", fir_solution)
    elif (a*(sec_solution**2) + (b*sec_solution) + c) == 0:
        if 'j' in str(fir_solution):
            print("The equation has 1 solution:", sec_solution)
        else:
            pass
    else:
        pass


quadratic_equation_input()
