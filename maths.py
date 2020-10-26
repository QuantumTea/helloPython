import math


def my_sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


def my_multiply(a, b):
    return a * b


def my_square(a):
    return a * a


def my_cube(a):
    return a * a * a


def factorial(a):
    return math.factorial(a)


def factorial_with_recursion(n):
    if n == 1:
        return n
    elif n < 1:
        return "NA"
    else:
        return n * factorial_with_recursion(n - 1)
