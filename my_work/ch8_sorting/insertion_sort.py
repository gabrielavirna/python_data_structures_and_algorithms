"""
Insertion sort
--------------

Running time:
-------------
Worst case: O(n^2);  Best case is O(n).
- considered stable in that it does not change the relative order of elements that have equal keys.
It also only requires no more memory than what is consumed by the list because it does the swapping in-place.

Implementation:
---------------
- uses the same idea as Bubble Sort: swapping adjacent elements to sort a list of items

Assume that a certain portion of the list has already been sorted, while the other portion remains unsorted.
Move through the unsorted portion of the list, picking one element at a time.  With this element, go through the
sorted portion of the list and insert it in the right order so that the sorted portion of the list remains sorted.

Consider the following array:

  5     |  1  100  2  10
[0]     | [1] [2] [3] [4]
sorted      unsorted

The algorithm starts by using a for loop to run between the indexes 1 and 4. We start from index 1 because we assume the
sub-array with index 0 to already be in the sorted order.

At the beginning of the execution of each run of the for loop, the element at unsorted_list[index] is stored in the
insert_value variable. Later, when we find the appropriate position in the sorted portion of the list, insert_value will
be stored at that index or location.
The while loop traverses the list backwards, guided by two conditions: first, if search_index > 0, then it means that
there are more elements in the sorted portion of the list; second, for the while loop to run,
unsorted_list[search_index-1] must be greater than the insert_value. The unsorted_list[search_index-1] array will do
either of the following things:
- Point to the element just before the unsorted_list[search_index] before the while loop is executed the first time
- Point to one element before unsorted_list[search_index-1] after the while loop has been run the first time
"""


def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]

        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            # moves the list traversal backwards till it bears the value 0
            search_index -= 1

        unsorted_list[search_index] = insert_value

    return unsorted_list


u_list = [5, 1, 100, 2, 10]
print(insertion_sort(u_list))