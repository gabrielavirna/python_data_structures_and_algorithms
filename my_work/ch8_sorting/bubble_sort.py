"""
Bubble sort
-----------
- very simple idea: Given an unordered list, we compare adjacent elements in the list, each time, putting in the right
order of magnitude, only two elements. The algorithm hinges on a swap procedure.

Take a list with only two elements:
 5   2
[0] [1]

To sort this list, swap them effectively into the right position with 2 occupying index 0 and 5 occupying index 1.
First, element 5 will be copied to a temporary location, temp. Then element 2 will be moved to index 0. Finally, 5 will
be moved from temp to index 1. At the end of it all, the elements will have been swapped. The list will contain: [2, 5].

Algorithm:
----------
- Swap these elements -> to swap effectively, use a temporary storage area:
- How many times to swap?
By swapping the adjacent elements in exactly len(unordered_list)-1 iterations, the largest number ends up at the last
position on the list. (for list [3, 2, 1] => 2 max iterations: [3, 2, 1] => [2, 3, 1] => [2, 1, 3]).
We recognize that a total of four comparisons at most were needed to get our list sorted.
Therefore, both inner and outer loops have to run len(unordered_list)-1 times for all elements to be sorted.

Running time:
------------
- Best case: O(n); Worst case: O(n^2) - The bubble sort is a highly inefficient sorting algorithm.

Generally, the bubble sort algorithm should not be used to sort large lists.
However, on relatively small lists, it performs fairly well.

There is a variant of the bubble sort algorithm where if there is no comparison within the inner loop, we simply quit
the entire sorting process. The absence of the need to swap elements in the inner loop suggests the list has already
been sorted. In a way, this can help speed up the generally considered slow algorithm.
"""


def bubble_sort(unordered_list):
    # by swapping the adjacent elements in exactly len(unordered_list)-1 iterations,
    # the largest number ends up at the last position on the list
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            # no needless swaps occur if two adjacent elements are already in the right order
            if unordered_list[j] > unordered_list[j + 1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
    return unordered_list


u_list = [1, 3, 2, 6, 4, 8, 5]
print(bubble_sort(u_list))