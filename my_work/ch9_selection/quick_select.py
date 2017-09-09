"""
Quick select (randomized selection algorithm)
- based on quick sort (ch8_sorting); used to obtain the ith-smallest element in an unordered list of items (e.g.numbers)

"""


def swap(unsorted_array, a, b):
    temp = unsorted_array[a]
    unsorted_array[a] = unsorted_array[b]
    unsorted_array[b] = temp


def partition(unsorted_array, first_index, last_index):
    # these 2 lines added, comparing to quick_sort partition
    # => there's only one element in our sublist => return any of the function parameters
    if first_index == last_index:
        return first_index

    # This choice to make the 1st element the pivot is a random decision.
    # It often does not yield a good split and subsequently a good partition.
    # However, the ith element will eventually be found.
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:

        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            swap(unsorted_array, greater_than_pivot_index, less_than_pivot_index)
        else:
            break

    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot

    # returns the pivot index pointed to by less_than_pivot_index
    return less_than_pivot_index


# parameters: the index of the first, the last, the ith element
def quick_select_helper(unsorted_array, left, right, k):
    #  returns the split index = the position in the unordered list where
    # all elements between right to split-1 are < the element contained in the array split,
    # while all elements between split+1 to left are greater.
    split_point = partition(unsorted_array, left, right)

    if split_point == k:
        return unsorted_array[k]

    # =>  the kth-smallest item should exist/be found between split+1 and right:
    elif split_point < k:
        return quick_select_helper(unsorted_array, split_point + 1, right, k)
    else:
        return quick_select_helper(unsorted_array, left, split_point - 1, k)


def quick_select(unsorted_array, k):
    quick_select_helper(unsorted_array, 0, len(unsorted_array) - 1, k)

u_array = [43, 3, 20, 4, 89, 77]
quick_select(u_array, 1)
print(u_array)
