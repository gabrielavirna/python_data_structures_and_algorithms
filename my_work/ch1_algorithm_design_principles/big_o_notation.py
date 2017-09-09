"""
Growth rates
-------------
(order low to high) (a.k.a. time complexity of a function/ complexity class of a function):

O(1)    -- Constant             -- append, get item, set item.
O(logn) -- Logarithmic          -- Finding an element in a sorted array.
O(n)    -- Linear               -- copy, insert, delete, iteration.
nLogn   -- Linear-Logarithmic   -- Sort a list, merge - sort.
n^2     -- Quadratic            -- Find the shortest path between two nodes in a graph. Nested loops.
n^3     -- Cubic                -- Matrix multiplication.
2^n     -- Exponential          -- 'Towers of Hanoi' problem, backtracking.


Composing complexity classes
----------------------------
* Simplest way to combine 2 complexity classes: add them:

E.g. Consider the two operations of inserting an element into a list and then sorting that list:
-> inserting an item: O(n) time
-> sorting: O(nlogn) time
==> Total time complexity: O(n + nlogn), choose the highest order term ==> O(nlogn)

* Multiply the complexity class by the number of times the operation is carried out.

E.g. If we repeat an operation, for example, in a while loop
-> If an operation with time complexity O(f(n)) is repeated O(n) times
==> The time complexity: O(f(n))*O(n) = O(n*f(n)))

* Multiplying the time complexity of the operation with the number of times this operation executes.
** The running time of a loop is at most: the running time of the statements inside the loop * the number of iterations.

E.g Suppose the function f(...) has a time complexity of O(n2) and it is executed n times in a while loop as follows:

    for i in range(n):
        f(...)

==> The time complexity of this loop:  O(n^2) * O(n) = O(n * n2) = O(n3)


E.g. A single nested loop (one loop nested inside another loop) will run in n^2 time assuming both loops run n times.

    for i in range(0,n):
        for j in range(0,n)
            #statements

==> Running time: each statement is a constant, c, executed nn times, cnn = cn^2 = O(n^2)

* For consecutive statements within nested loops:
we add the time complexities of each statement and multiply by the number of times the statement executed

E.g.

    n = 500    #c0
    #executes n times
    for i in range(0,n):
        print(i)    #c1
    #executes n times
    for i in range(0,n):
        #executes n times
        for j in range(0,n):
        print(j)   #c2

==> Time complexity: c0 +c1n + cn^2 = O(n^2).


* We can define (base 2) logarithmic complexity, reducing the size of the problem by ½, in constant time.

E.g.

    i = 1
    while i <= n:
        i=i * 2
        print(i)

-> i is doubling on each iteration, if n = 10, it prints out 4 numbers; 2, 4, 8, and 16.
-> if we double n, it prints out 5 numbers
-> With each subsequent doubling of n the number of iterations is only increased by 1.
==> The total time complexity: O(log(n)).
"""