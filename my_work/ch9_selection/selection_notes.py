"""
Selection Algorithms
--------------------
- set of algorithms related to finding elements in an unordered list of items
- selecting the median of a set of numbers and selecting the ith-smallest or -largest element in a list

Selection types:
----------------
Selection by sorting
Randomized selection
Deterministic selection

I. Selection by sorting
-----------------------
Items in a list may undergo statistical enquiries such as finding the mean, median, and mode values.

Finding the mean & mode values: do not require the list to be ordered.
Finding the median: the list must first be ordered; requires to find the element in the middle pos. of the ordered list.
Finding the last-smallest item in the list or the first-smallest item in the list?

To find the ith-smallest number in an unordered list of items: obtain the index of where that item occurs; but the
elements not sorted => difficult to know whether the element at index 0 in a list is really the first-smallest number.

When dealing with unordered lists: sort the list (pragmatic & obvious thing to do).
Once the list is sorted => sure that the 0th element in the list will house the first-smallest element in the list.
Likewise, the last element in the list will house the last-smallest element in the list.

Assume that the luxury of sorting before performing the search cannot be afforded =>
Is it possible to find the ith-smallest element without having to sort the list in the first place?


II. Randomized selection (quick select)
---------------------------------------
-  used to obtain the ith-smallest element in an unordered list of items; based on quick sort (ch8_sorting), that allows
us to sort an unordered list of items, but has a way of preserving the index of elements as the sorting algorithm runs.

The quick sort algorithm steps: Selects a pivot; Partitions the unsorted list around the pivot;
Recursively sorts the two halves of the partitioned list using step 1 and step 2.

-> note that after every partitioning step, the index of the pivot won't change even after the list has become sorted.
=> this property enables us to be able to work with a not-so-fully sorted list to obtain the ith-smallest number.
"""