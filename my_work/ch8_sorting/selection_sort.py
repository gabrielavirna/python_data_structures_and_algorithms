"""
Selection sort
--------------
- sorting algorithm simple to understand, yet also inefficient

Running time: worst and best asymptotic values: O(n^2).
-------------

Implementation:
---------------
It begins by finding the smallest element in an array and interchanging it with data at, for instance, array index [0].
The same operation is done a second time; however, the smallest element in the remainder of the list after finding the
first smallest element is interchanged with the data at index [1].

E.g.
Sort a list of numbers:
 5   2   65  10
[0] [1] [2] [3]

Starting at index 0, we search for the smallest item in the list that exists between index 1 and the index of the last
element. When this element has been found, it is exchanged with the data found at index 0. We simply repeat this process
until the list becomes sorted.
"""


# Selection sort algorithm
# puts the unsorted list of items in ascending order of magnitude
def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)

    # outer loop -> to go through the list
    for i in range(size_of_list):   # from 0 up to size_of_list-1
        # inner loop -> to go through the list & make the necessary swap any time
        for j in range(i+1, size_of_list):  # from i+1 up to size_of_list-1

            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp

    return unsorted_list


u_list = [5, 2, 65, 10]
print(selection_sort(u_list))

