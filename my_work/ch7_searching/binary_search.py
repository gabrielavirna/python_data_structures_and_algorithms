"""
Binary search
-------------
- Worst time complexity: O(log n); The half-ing of the list on each iteration follows a log n of the number
of elements progression (log x is assumed to be log base 2).
- a search strategy used to find elements within an ordered list of items
- by consistently reducing the amount of data to be searched => increasing the rate at which the search term is found.

Algorithm steps:
- A binary decision has to be made at each attempt to find an item in the list. One critical decision is to guess which
part of the list is likely to house the item we are looking for. Would the search term be in the first half or second
half of the list, that is, if we always perceive the list as being comprised of two parts?

Instead of moving from one cell of the list to the other, if we employ the use of an educated guessing strategy,
we are likely to arrive at the position where the item will be found much faster.

E.g. to find the middle page of a 1000 page book. We already know that every book has its pages numbered sequentially
from 1 upwards. So it figures that the 500th page should be found right at the middle of the book, instead of moving
and flipping from page 1, 2 to reach the 500th page. Let's say we decide to now look for the page 250. We can still
use our strategy to find the page easily. We guess that page 500 cuts the book in half. Page 250, will lay to the
left of the book. No need to worry about whether we can find 250th page between page 500 and 1000 because it can
never be found there. So using page 500 as reference, we can open to about half of the pages that lay between the
1st and 500th page. That brings us closer to finding the 250th page.
"""


# I. Binary search on an ordered list - iterative
def binary_search_it(ordered_list, search_term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        # find the middle index and compare it with the search item
        mid_point = int((index_of_first_element + index_of_last_element)/2)

        if ordered_list[mid_point] == search_term:
            return mid_point
        elif search_term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    if index_of_first_element > index_of_last_element:
        return None


# II.  Binary search on an ordered list - recursive
def binary_search(ordered_list, first_element_index, last_element_index, search_term):
    if last_element_index < first_element_index:
        return None
    else:
        mid_point = int(first_element_index + (last_element_index - first_element_index)/2)

        if search_term > ordered_list[mid_point]:
            return binary_search(ordered_list, mid_point + 1, last_element_index, search_term)
        elif search_term < ordered_list[mid_point]:
            return binary_search(ordered_list, first_element_index, mid_point - 1, search_term)
        else:
            return mid_point


store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search_it(store, 2))
print(binary_search(store, 0, 7, 2))



