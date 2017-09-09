import time

"""
Dynamic programming
-------------------
- a problem is broken down into smaller problems (similar to D&Q)
- make sure not to compute the solution to an already encountered subproblem (sounds a bit like recursion, but things
are a little broader here). A problem may lend itself to being solved by using dynamic programming but will not
necessarily take the form of making recursive calls.

Problem to solve with dynamic programming
- has the property: it should have an overlapping set of subproblems (repeated calls to a function with the same
parameters and output). Once we realize that the form of subproblems has repeated itself during computation, we need not
compute it again. Instead, we return the result of a pre-computed value of that subproblem previously encountered.

To avoid to re-evaluate a subproblem, there are 2 efficient techniques that store the results of each subproblem:

 -> I. Memoization
-------------------
- starts from the initial problem set and divides it into small subproblems.
After the solution to a subprogram has been determined, we store the result to that particular subproblem.
In the future, when this subproblem is encountered, we only return its pre-computed result.

-> II. Tabulation
------------------
- approach: fill a table of solutions to subproblems and then combine them to solve bigger problems.
- involves the use of a table of results or matrix in some cases to store results of computations for later use.
- approach solves the bigger problem by first working out a route to the final solution. 
"""

# Problem: find the ith term of the Fibonacci series


# Recursion technique
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# I. Memoization technique
# This algorithms runs much faster than recursion; it sacrificed space complexity
# for time because of the use of memory in storing the result to the function calls.
def fib_mem(n, lookup):
    if n <= 2:
        lookup[n] = 1

    if lookup[n] is None:
        lookup[n] = fib_mem(n-1, lookup) + fib_mem(n-2, lookup)
    return lookup[n]


# II. Tabulation technique
def fib_tab(n):
    # develop a table with the values of fib(1) and fib(2) predetermined.
    # Based on these two values, we will work our way up to fib(n):
    results = [1, 1]

    for i in range(2, n):
        results.append(fib_tab(i-1) + fib_tab(i-2))
    return results[-1]


# Recursive technique
# the time it takes for fib() to perform
start1 = time.time()
fib(50)
print("Time it takes to fib() to find the i-th term: %f" % (time.time() - start1))
# print(fib(50))

# Memoization technique:
# create a list of 1,000 elements, that will store the value of
# the computation of the various calls to the fib_dynamic() function:
start2 = time.time()
map_set = [None] * 10000
fib_mem(50, map_set)
print("time it takes to fib_mem() to find the i-th term: %f" % (time.time() - start2))
# print(fib_mem(100, map_set))

# Tabulation technique
start3 = time.time()
fib_tab(50)
print("Time it takes to fib_tab() to find the i-th term: %f" % (time.time() - start3))

