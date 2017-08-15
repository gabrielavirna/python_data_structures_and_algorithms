"""
Algorithm design paradigms:

- Divide and conquer
- Greedy algorithms
- Dynamic programming


-> D&Q: involves breaking a pb. into smaller independent sub pbs & combining the results to obtain a global solution;
        uses recursion

-> Greedy: involves finding the best solution to a local problem in the hope that this will lead to a global solution;
           involve optimization and combinatorial problems, e.g. Travelling Salesman problem - shortest path strategy

-> Dynamic: intermediate results are cached and can be used in subsequent operations;
            allows us to compare results at different stages; used when our sub problems overlap.


Analysing alg => Asymptotic analysis / Time complexity: relationship between the time it takes to complete a certain
computation & the size of the input to that comp. What happens when the input, the no. of digits, n, is very large?

Runtime analysis: math. relationship between n, the size of the input, and the time it takes for the algorithm to run.
Worst case analysis: it gives us a tight upper bound that our algorithm is guaranteed not to exceed.

Runtime analysis: see merge sort

"""