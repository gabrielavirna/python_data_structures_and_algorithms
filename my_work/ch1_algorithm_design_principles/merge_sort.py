"""
Merge Sort:
-----------
recursive algorithm that uses a divide and conquer approach: breaking the problem into smaller sub problems,
recursively solving them, and then somehow combining the results.

1.Recursively sort the left half of the input array.
2.Recursively sort the right half of the input array.
3.Merge two sorted sub arrays into one.

Runtime analysis: using mathematical expressions, essentially adding and multiplying operations.
Merge sort:
-----------------------------
Level 0: initial recursive call
Level 1: the problem is split into 2 * n/2 sub problems
Level 2: there is 4 * n/4 sub problems = 2^2 * n/2^2
.......................................
Level log2(n): 2^j * n/2^j (when does it reach its base case: when the array = {0, 1}

==> Total number of levels: log2n + 1
==> For level j , where j is an integer 0, 1, 2 ... log2n, there are  2^j sub problems each of size n/2^j.


To calculate the total number of operations: know the no. of operations encompassed by a single merge of two sub arrays:
1) 3 assignment operations,
2) 3 while loops.
    1st loop -> if else statement and within each of are 2 operations: a comparison, then an assignment
    =>  2 operations carried out m times.
3) 2 while loops with 1 assignment operation each

==> Total of operations: 4m + 3 for each recursion of merge sort.
==> The upper bound for the number of operations: is 7m, since m must be at least 1,.
==> Maximum number of operations at each level of the recursion tree: 2^j * 7(n/2^j) = 7n
    the number of sub problems * the number of operations in each sub problem
==> Total number of operations for a complete merge sort: 7n(log2(n) + 1) = 7n*log2(n) + 7n = 7n*log2(n) + 7
    the number of operations on each level * the number of levels
"""


def merge_sort(my_array):
    # base case if the input array is one or zero just return.
    if len(my_array) > 1:
        # splitting input array
        mid = len(my_array) // 2
        left = my_array[:mid]
        right = my_array[mid:]

        # recursive calls to merge_sort for left and right sub arrays
        merge_sort(left)
        merge_sort(right)
        # 3 initialization operations
        i = j = k = 0
        # Traverse and merges the sorted arrays
        while i < len(left) and j < len(right):
            # if left < right comparison operation
            if left[i] < right[j]:
                # if left < right Assignment operation
                my_array[k] = left[i]
                i += 1
            # if right <= left assignment
            else:
                my_array[k] = right[j]
                j += 1
            k = k + 1

        while i < len(left):
            # Assignment operation
            my_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            # Assignment operation
            my_array[k] = right[j]
            j += 1
            k += 1

    print('merging', my_array)
    return

print(merge_sort([11, 22, 88, 33, 66, 55, 77, 44]))