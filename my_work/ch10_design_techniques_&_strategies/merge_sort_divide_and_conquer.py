"""
Divide and conquer
-------------------
- emphasizes the need to break down a problem into smaller problems of the same type/form of the original problem.
- These subproblems are solved and combined to solve the original problem.

Implementation - 3 steps:
-> Divide: break down an entity/problem (the original problem into subproblems) => through iterative/recursive calls.

-> Conquer: It's impossible to continue to break the problems into subproblems indefinitely. At some point, the smallest
indivisible problem will return a solution. Once this happens, we can reverse our thought process and say that if we
know the solution to the smallest problem possible, we can obtain the final solution to the original problem.

-> Merge: to obtain the final solution, combine the smaller solutions to the smaller problems in order to solve the
bigger problem. Other variants to D & Q: merge and combine, conquer and solve.

Algorithms that use D & Q principle: merge sorting, quick sort, and Strassen's matrix multiplication.

Merge sort
----------
- based on D & Q rule
- Divide: split the list of unsorted elements into ~ 2 halves; continue to divide the 2 halves recursively;
- Conquer:  After a while, the sublists created as a result of the recursive call will contain only 1 element;
  At that point, begin to merge the solutions in the conquer or merge step:
"""


# Divide step
def merge_sort(unsorted_list):
    # if list has only 1 element, return it
    if len(unsorted_list) == 1:
        return unsorted_list
    else:
        # find the approximate middle
        mid_point = int(len(unsorted_list)/2)
        first_half = unsorted_list[:mid_point]
        second_half = unsorted_list[mid_point:]

        # recursive call: by passing the 2 sublists to merge_sort() again:
        half_a = merge_sort(first_half)
        half_b = merge_sort(second_half)

        return merge(half_a, half_b)


# Merge step
def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []

    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1

    # adds the elements that may be left behind in first_sublist/second_sublist
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1

    # return the sorted list
    return merged_list


u_list = [4, 6, 8, 5, 7, 11, 40]
print(merge_sort(u_list))




