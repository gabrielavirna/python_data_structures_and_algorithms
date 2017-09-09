"""
Design Techniques and Strategies
--------------------------------
In the world of algorithms, there are a plethora of techniques and design principles.
A working knowledge and mastery of these techniques is required to tackle harder problems in the field.

Classification of algorithms
----------------------------
- There are classification schemes that are based on the goal that an algorithm has to achieve.
Question: do these algorithms share the same form?
If yes, what are the similarities & characteristics used as a basis? If no, can the algorithms be grouped into classes?

I. Classification by implementation
-----------------------------------
When translating a series of steps or processes into a working algorithm, there are a number of forms that it may take.
The heart of the algorithm may employ some assets.

-> Recursion (vs Iterative)
---------------------------
- Recursive algorithms: make calls to themselves until a certain condition is satisfied.
Some problems are more easily expressed by implementing their solution through recursion (Towers of Hanoi).
Different types: some include single & multiple/indirect/anonymous/generative recursion.

- Iterative algorithms: use a series of steps or a repetitive construct to formulate a solution.
This repetitive construct could be a simple while loop/any other kind of loop.
Iterative solutions also come to mind more easily than their recursive implementations.

-> Logical
-----------
One implementation of an algorithm is expressing it as a controlled logical deduction. This logic component is comprised
of the axioms that will be used in the computation. The control component determines the manner in which deduction is
applied to the axioms => expression: algorithm = logic + control => the basis of the logic programming paradigm.

The logic component determines the meaning of the algorithm. The control component only affects its efficiency.
Without modifying the logic, the efficiency can be improved by improving the control component.

-> Serial or parallel
---------------------
The RAM model of most computers allows for the assumption that computing is done one instruction at a time.
- Serial algorithms(sequential algorithms): algorithms that are executed sequentially.
  Execution commences from start to finish without any other execution procedure.

- Parallel algorithms: perform more than one operation (several instructions) at a time .
In the PRAM model, there are serial processors that share a global memory. The processors can also perform various
arithmetic and logical operations in parallel. This enables the execution of several instructions at one time.

The parallel/distributed algorithms: divide a problem into subproblems among its processors to collect the results.
Some sorting algorithms can be efficiently parallelized, while iterative algorithms are generally parallelizable.

-> Deterministic vs nondeterministic
------------------------------------
Deterministic algorithms: will produce the same output without fail every time the algorithm is run with the same input.
There are some sets of problems that are so complex in the design of their solutions that expressing their solution in a
deterministic way can be a challenge.

Nondeterministic algorithms: can change the order of execution or some internal subprocess that leads to a change in the
final result any time the algorithm is run. As such, with every run of a nondeterministic algorithm, the output of the
algorithm is different. For instance, an algorithm that makes use of a probabilistic value will yield different outputs
on successive execution depending on the value of the random number generated.


II. Classification by complexity
---------------------------------
To determine the complexity of an algorithm:
try to estimate how much space (memory) and time is used overall during the computation or program execution.

Complexity curves
-----------------
Now consider a problem of magnitude n. T(n): Time complexity of an algorithm. O(n): the growth rate of an algorithm.
List of runtimes from better to worse: O(1), O(log n), O(n), O(n log(n)), O(n^2), O(n^3), or O(2^n).
Depending on the steps an algorithm performs, the time complexity may or may not be affected.


A practical scenario:
By which means do we arrive at the conclusion that the bubble sort algorithm is slower than the quick sort algorithm?
Or in general, how do we measure the efficiency of one algorithm against the other?
=> compare the Big O of any number of algorithms to determine their efficiency.
This approach gives us a time measure or the growth rate, which charts the behavior of the algorithm as n gets bigger.


III. Classification by design
-----------------------------
A given problem may have a number of solutions.
When the algorithms of these solutions are analyzed, it becomes evident that some implement a certain technique/pattern.

-> Divide and conquer
---------------------
- To solve (conquer) certain problems: this algorithm divides the problem into subproblems (smaller chunks, division is
mostly done by recursion) identical to the original problem that can easily be solved.
Solutions to the subproblems are combined in such a way that the final solution is the solution of the origin problem.

- Algorithms that use this technique: merge sort, quick sort, and binary search.

-> Dynamic programming
----------------------
- Divide and conquer : a problem is broken down into smaller problems.
Each subproblem has to be solved before its results can be used to solve bigger problems.

- Dynamic programming -  a problem is broken down into smaller problems, but it does not compute the solution to an
already encountered subproblem. Rather, it uses a remembering technique to avoid the recomputation.
Dynamic programming problems have two characteristics: optimal substructure and overlapping subproblem.

-> Greedy algorithms
--------------------
Optimal solution:
For a certain category of problems, determining the best solution is really difficult. To make up for the lack of
optimal solution, we resort to an approach where we select out of a bunch of options or choices the closest solution
that is the most promising in obtaining a solution.

Greedy algorithms:
- much easier to conceive -> the guiding rule:
always select the solution that yields the most benefit and continue doing that, hoping to reach a perfect solution.
- This technique aims to find a global optimal final solution by making a series of local optimal choices.
The local optimal choice seems to lead to the solution. In real life, most of those local optimal choices made are
suboptimal. As such, most greedy algorithms have a poor asymptotic time complexity.

Examples: Prim's algorithm for finding the minimum spanning trees, the Knapsack problem,Travelling Salesman problem.
"""