"""
Greedy algorithms
- make decisions that yield the largest benefit in the interim.
- Aim: that by making these high yielding benefit choices, the total path will lead to an overall good solution or end.

Coin-counting problem
---------------------
In some arbitrary country, we have the denominations 1 GHC, 5 GHC, and 8 GHC.
Given an amount such as 12 GHC, find the least possible number of denominations needed to provide change.

Using the greedy approach:
- pick the largest value from our denomination to divide 12 GHC -> * yields the best possible means by which we can
reduce the amount 12 GHC into lower denominations. The remainder, 4 GHC, cannot be divided by 5, so try the 1 GHC
denomination and realize that we can multiply it by 4 to obtain 4 GHC.
=> the least possible number of denominations to create 12 GHC is to get a one 8 GHC and four 1 GHC notes.
"""


# Greedy algorithm: returns the respective denominations
def basic_small_change(denominations, total_amount):
    sorted_denoms = sorted(denominations, reverse=True)
    no_of_denoms = []

    # starts by using the largest denomination
    for denom in sorted_denoms:
        # the quotient
        div = int(total_amount / denom)
        # updated to store the remainder for further processing
        total_amount = total_amount % denom

        if div > 0:
            no_of_denoms.append((denom, div))

    return no_of_denoms


# Better greedy algorithm: returns a list of tuples that allow to investigate the better results
def optimal_small_change(denominations, total_amount):
    sorted_denoms = sorted(denominations, reverse=True)
    series = []

    # to limit the denominations from which we find the solution
    for j in range(len(sorted_denoms)):
        # slicing [5, 4, 3] => [5,4,3], [4,3], [3]
        term = sorted_denoms[j:]

        no_of_denoms = []
        local_total = total_amount
        for den in term:
            div = int(local_total / den)
            local_total = local_total % den
            if div > 0:
                no_of_denoms.append((den, div))

        series.append(no_of_denoms)

    return series


print(basic_small_change([1, 5, 8], 12))
print(optimal_small_change([1, 5, 8], 12))

# algorithm fails: doesn't give the optimal solution
print(basic_small_change([1, 5, 8], 14))
# The right optimal solution: two 5 GHC and two 1 GHC denominations
print(optimal_small_change([1, 5, 8], 14))
