"""
Linear Search - technique to find an element in the list
-------------
- performed on a typical Python list; the list has elements that are accessible through the list index.
- technique traverses the list of elements, by using the index to move from the beginning of the list to the end.
    Each element is examined and if it does not match the search item, the next item is examined.
    By hopping from one item to its next, the list is traversed sequentially.

E.g.
list :  60   1  88  10  11  100
index: [0]  [1] [2] [3] [4] [5]

I.Unordered linear search
-------------------------
- Worst case running time: O(n) - All the elements may need to be visited before finding the search term.
This will be the case if the search term is located at the last position of the list.

E.g. An unordered list: 60, 1, 88, 10, and 100. The items in the list have no order by magnitude.

The algorithm steps:
- one proceeds from the very first item, compares that with the search item. If a match is not made the next element
in the list is examined. This continues till we reach the last element in the list or until a match is made.

II. Ordered linear search
--------------------------
- The worst case time complexity: O(n) -  In general inefficient especially when dealing with large data sets.
- when the elements of a list have been already sorted, the search algorithm can be improved.

- Assuming the elements have been sorted in ascending order, the search operation can take advantage of the ordered
nature of the list to make search more efficient.

The search algorithm steps:
- Move through the list sequentially. If a search item is greater than the object or item currently under inspection
in  the loop, then quit and return None. In the process of iterating through the list, if the search term is greater
than the current item, then there is no need to continue with the search.
"""


# I. Unordered linear search
def unordered_linear_search(unordered_list, search_term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        # test if the search term is equal to the item that the index points to.
        if search_term == unordered_list[i]:
            return i

    return None


# II. Ordered linear search
def ordered_linear_search(ordered_list, search_term):
    ordered_list_size = len(ordered_list)

    for i in range(ordered_list_size):
        if search_term == ordered_list[i]:
            return i
        # if the current item > the search term => no need to further search the list.
        elif ordered_list[i] > search_term:
            return None
