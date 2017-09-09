"""
Quick sort
----------
- the algorithm falls under the divide and conquer class of algorithms
- D&Q: break (divide) a problem into smaller chunks that are much simpler to solve (conquer) =>
  an unsorted array is broken into sub-arrays that are partially sorted, until all elements in the list are in the right
  position, by which time our unsorted list will have become sorted.

Worst case complexity: O(n^2),  but it is efficient when sorting large amounts of data.
---------------------

Implementation:
--------------
Select a pivot.
Partition the unsorted list around the pivot.
Recursively sort the two halves of the partitioned list using step 1 and step 2.


List partitioning
-----------------
- before we divide the list into smaller chunks, we have to partition it. This is the heart of the quick sort algorithm.
- To partition the array: first select a pivot. All the elements in the array will be compared with this pivot.
  At the end of the partitioning process, all elements that are less than the pivot will be to the left of the pivot,
  while all elements greater than the pivot will lie to the right of the pivot in the array.

Pivot selection
---------------
- for simplicity, take the first element in any array as the pivot; this pivot selection degrades in performance,
especially when sorting an already sorted list. Randomly picking the middle or last element in the array as the pivot
does not improve the situation any further.
"""


def swap(unsorted_array, a, b):
    temp = unsorted_array[a]
    unsorted_array[a] = unsorted_array[b]
    unsorted_array[b] = temp


def partition(unsorted_array, first_index, last_index):
    # This choice to make the 1st element the pivot is a random decision.
    # It often does not yield a good split and subsequently a good partition.
    # However, the ith element will eventually be found.
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element  # right index (left movement <-)
    greater_than_pivot_index = first_index + 1     # left index (right movement ->)

    while True:
        # move right if smaller/eq than/to pivot
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        # move left if greater/eq than/to pivot
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        # indices stopped moving: swap the element at those indexes
        if greater_than_pivot_index < less_than_pivot_index:
            swap(unsorted_array, greater_than_pivot_index, less_than_pivot_index)
        else:
            break

    # place pivot back in the right place:
    # all values < pivot are to its left &  all values > pivot are to its right
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot

    # returns the pivot index pointed to by less_than_pivot_index
    return less_than_pivot_index


def quick_sort_helper(unsorted_array, first, last):
    if first < last:
        # partition_point in the unsorted_array: where all elements to the left are
        # less than the pivot and all elements to its right are greater than it.
        partition_point = partition(unsorted_array, first, last)
        # Using the split point, recursively sort the 2 sub-arrays
        quick_sort_helper(unsorted_array, first, partition_point - 1)
        quick_sort_helper(unsorted_array, partition_point + 1, last)
    # return unsorted_array


def quick_sort(unsorted_array):
    quick_sort_helper(unsorted_array, 0, len(unsorted_array) - 1)


u_array = [43, 3, 20, 4, 89, 77]
quick_sort(u_array)
print(u_array)
