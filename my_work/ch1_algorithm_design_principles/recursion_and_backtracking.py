"""
Recursive function:     -> base cases - which tell the recursion when to terminate,
                        -> recursive cases - that call the function they are in


Backtracking: a divide and conquer method for exhaustive search.

Backtracking: a form of recursion that is particularly useful for pbs such as traversing tree structures,
              where we are presented with a number of options at each node, from which we must choose one.
              Subsequently we are presented with a different set of options, and depending on the series of choices
              made either a goal state or a dead end is reached.
              If it is the latter, we must backtrack to a previous node and traverse a different branch.


--> factorial(n):  The recursive factorial algorithm-: 2 cases: base case: when n = 0; recursive case: when n > 0
--> bit_str(n, s): Generating all the possible permutations of a given string, s, of a given length n
 """


def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # make a calculation and a recursive call
        f = n * factorial(n - 1)
        print(f)
        return f


factorial(4)  # factorial(4) requires 4 recursive calls + the initial parent call.


def bit_str(n, s):
    if n == 1:
        return s
    else:
        return [digit + bits for digit in bit_str(1, s) for bits in bit_str(n - 1, s)]


print(bit_str(3, 'abc'))

"""This recursive implementation demands that the function compute all perms before returning the full list 
=> inconvenient: super exponential space requirements of the above algorithm"""


def permutations(string):
    if not string:
        return ['']
    result = []
    for i, d in enumerate(string):
        perms = permutations(string[:i] + string[i + 1:])
        for perm in perms:
            result.append(d + perm)
    return result


print(permutations("123"))

"""Better: Use Generators: they yield values rather than return them, which means their execution state is saved and 
halted, including entire stack frames. The ability to freeze recursive calls allows for powerful and expressive code."""


def permutations_with_generators(string):
    if not string:
        yield ''
    for i, d in enumerate(string):
        perms = permutations(string[i:] + string[:i + 1])
        for perm in perms:
            yield d + perm


# print(permutations_with_generators("xyz"))
# for perm in permutations_with_generators("xyz"):
#   print(perm)

"""Generating all combinations is similar. 
Return breaks out of its function, whereas yield falls through to the subsequent statements."""


def combinations(string):
    if not string:
        yield ''
    for i, d in enumerate(string):
        combs = combinations(string[i + 1:])
        for comb in combs:
            yield d + comb


for comb in combinations("4567"):
    print(comb)
