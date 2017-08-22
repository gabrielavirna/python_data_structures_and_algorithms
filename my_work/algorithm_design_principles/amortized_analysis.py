import timeit
import matplotlib.pyplot as plt

"""
Amortized analysis:

- not so interested in the time complexity of individual operations, but rather the time averaged running time of
sequences of operations; an take into account the state change of data structures

- finds an upper bound on runtime by imposing an artificial cost on each operation in a sequence of operations, and
then combining each of these costs.

* Algorithm analysis: Two other common approaches - need to know what the typical or expected data sets are.

->  Average case analysis:
    finds the average running time based on some assumptions regarding the relative frequencies of various input values
->  Benchmarking:
    having an agreed set of typical inputs that are used to measure performance


Benchmark an algorithm's runtime performance:
---------------------------------------------
- timing how long the algorithm takes to complete given various input sizes

Measuring runtime performance is dependent on the hardware that it is run on => faster processors will give better
results, however, the relative growth rates as we increase the input size will retain characteristics of the algorithm
itself rather than the hardware it is run on.


E.g. a nested loop.
The time complexity of this algorithm: O(n^2),
since for each n iterations in the outer loop there are also n iterations in the inter loop.
Our simple nested for loop consists of a simple statement executed on the inner loop:"""


def nest(n):
    for i in range(n):
        for j in range(n):
            i + j


""" Simple test function that runs the nest function with increasing values of n. 
With each iteration we calculate the time this function takes to complete using the timeit.timeit function. 
The timeit function takes 3 arguments, a string representation of the function to be timed, a setup function that 
imports the nest function, and an int parameter that indicates the number of times to execute the main statement. 

Time the nest function takes to complete relative to the input size, n => sufficient to call the nest function once on 
each iteration. The following function returns a list of the calculated runtimes for each value of n:"""


def test2(n):
    ls = []
    for n in range(n):
        t = timeit.timeit("nest(" + str(n) + ")", setup="from __main__ import nest", number=1)
        ls.append(t)
    return ls


""" Run the test2 function and graph the results, together with the appropriately scaled n^2 function for comparison """
n = 10000
plt.plot(test2(n))
plt.plot([x * x / 10000000 for x in range(n)], label='n^2')
plt.legend(loc='upper left')
plt.show()

