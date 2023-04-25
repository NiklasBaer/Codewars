def sum_factorial(lst):
    total = 0
    for num in lst:
        factorial = 1
        for i in range(1, num+1):
            factorial *= i
        total += factorial
    return total

