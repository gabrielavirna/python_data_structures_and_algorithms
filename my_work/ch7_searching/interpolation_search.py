"""
Interpolation search
--------------------
- time complexity: O( log ( log n))
- another variant of the binary search algorithm that may mimic more, how humans perform search on any list of items.
- still based off trying to make a good guess of where in a sorted list of items, a search item is likely to be found.

- A more human thing: pick a middle element in a such a way as to not only split the array in half but to get as close
as possible to the search term.

E.g.
Given our search list: 44, 60, 75, 100, 120, 230 and 250,
the nearest_mid will be computed with the following values:

lower_bound_index = 0
upper_bound_index = 6
input_list[upper_bound_index] = 250
input_list[lower_bound_index] = 44
search_value = 230
=> mid_point will receive the value 5, which is the index of the location of our search term.
A binary search would have chosen 100 as the mid which will require another run of the algorithm.


Binary search vs. interpolation algorithm
=========================================

Take the list with elements: [ 2, 4, 5, 12, 43, 54, 60, 77]
At index 0 is stored 2 and at index 7 is found the value 77. Now, assume that we want to find the element 2 in the list.
How will the two different algorithms go about it?

If we pass this list to the interpolation search function, the nearest_mid function will return a value equal to 0.
Just by one comparison, we would have found the search term.

On the other hand, the binary search algorithm would need three comparisons to arrive at the search term.
The first mid_point calculated is 3. The 2nd mid_point is 1 and the last mid_point where the search term is found is 0.
"""


# formula brings us close to the search term.
def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + ((upper_bound_index - lower_bound_index) /
                               (input_list[upper_bound_index] - input_list[lower_bound_index])) * \
                                (search_value - input_list[lower_bound_index])


def interpolation_search(ordered_list, search_term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element < index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, search_term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

        if search_term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        elif search_term < ordered_list[mid_point]:
            index_of_last_element = mid_point - 1
        else:
            return mid_point

    if index_of_first_element > index_of_last_element:
        return None


