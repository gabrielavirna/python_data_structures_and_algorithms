"""
Recursion:
    Terminates when a base case is reached
    Each recursive call requires space in memory
    An infinite recursion results in a stack overflow error
    Some problems are naturally better suited to recursive solutions

Iteration:
    Terminates when a defined condition is met
    Each iteration is not stored in memory
    An infinite iteration will run while the hardware is powered
    Iterative solutions may not always be obvious"""


def iter_test(low, high):
    while low <= high:
        print(low)
        low += 1


def rec_test(low, high):
    if low <= high:
        print(low)
        rec_test(low+1, high)


iter_test(3, 5)
rec_test(3,5)