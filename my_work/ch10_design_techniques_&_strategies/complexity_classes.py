"""
Complexity classes
------------------
In an ideal world, each computational problem would be classified by its use of computational resources.
The problems that computer algorithms try to solve fall within a range of difficulty by which their solutions are
arrived at. Complexity classes: N, NP, NP-complete, and NP-hard problems.

P vs. NP
=========
The advent of computers has sped up the rate at which certain tasks are performed. In general, computers are good
at perfecting the art of calculation and all problems that can be reduced to a set of mathematical computations.
However, there are some nature or classes of problems that just take an enormous amount of time for the computer to
make a sound guess, let alone find the right solution.

-> P-type problems (polynomial time)-> relatively easy to solve problems;
It's the class of problems that computers can solve within polynomial time using a step-wise process of logical steps.

-> NP-Type problems (nondeterministic polynomial time) -> very hard to solve: "hard problem" refers to the way in which
problems increase in difficulty when trying to find a solution. However, despite the high growth rate of difficulty of
these problems, it's possible to determine whether a proposed solution solves the problem in polynomial time.


The Travelling Salesman problem
-------------------------------
- NP-Type problem;
- There are n no. of cities in a country, find the shortest route between all the cities & make the trip cost-effective.
- When the number of cities is small, this problem can be solved in a reasonable amount of time.
  However, when the number of cities is above any two-digit number, the time taken by the computer is remarkably long.

RSA encryption algorithm: A lot of computer systems and cybersecurity is based on it; the strength of the algorithm and
its security: it is based on the integer factoring problem, which is an NP-Type problem.

Finding the prime factors of a prime number composed of many digits is very difficult.
When two large prime numbers are multiplied, a large non-prime number is obtained with only two large prime factors.
Factorization of this number is where many cryptographic algorithms borrow their strength.


- Q. Does N = NP? A. The proof for N = NP is one of the Millennium Prize Problems for a correct solution (7 problems).

All P-type problems are subsets of NP problems
-----------------------------------------------
i.e. any problem that can be solved in polynomial time can also be verified in polynomial time.

- Q. Does P = NP? i.e. problems that can be verified in polynomial time can also be solved in polynomial time?
If they are equal, it would mean that problems that are solved by trying a number of possible solutions can be
solved without the need to actually try all the possible solutions, invariably creating some sort of shortcut proof.
- If such a proof is ever discovered, it will be a game-changer in fields as: cryptography, game theory, mathematics.

NP-Hard
========
A problem is NP-Hard if all other problems in NP can be polynomial time reducible or mapped to it.

NP-Complete
============
A problem is considered an NP-complete problem if it is first of all an NP hard and is also found in the NP class.
- the hardest problems in NP, an exponential-time problem; contains many hundreds of important combinatorial problems.
"""