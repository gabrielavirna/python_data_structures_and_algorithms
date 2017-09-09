"""
Searching
---------
- searching is one critical operation performed on data structures
- there are different strategies that can be used to find elements in a collection of items.

- One other important operation that makes use of searching is sorting.
It is virtually impossible to sort without some variant of a search operation. The "how of searching"
is also important as it has a bearing on how quick a sorting algorithm ends up performing.

Searching algorithms - 2 types:
--------------------
-> One category assumes that the list of items to apply the searching operation on, has already been sorted
-> The other category does not.

- The performance of a search operation:
heavily influenced by whether the items about to be searched have already been sorted or not.


Choosing a search algorithm
----------------------------
The binary search and interpolation search operations are better in performance than both ordered and unordered linear
search functions. Because of the sequential probing of elements in the list to find the search term, ordered and
unordered linear search have a time complexity of O(n). This gives very poor performance when the list is large.

The binary search operation on the other hand, slices the list in two, anytime a search is attempted. On each iteration,
we approach the search term much faster than in a linear strategy. The time complexity yields O(log n).
Despite the speed gain in using binary search, it is most it can not be used on an unsorted list of items neither is it
advised to be used for list of small sizes.

The ability to get to the portion of the list that houses a search term determines to a large extent, how well a search
algorithm will perform. In the interpolation search algorithm, the mid is calculated for which gives a higher
probability of obtaining our search term. The time complexity of the interpolation search is O( log ( log n)).
This gives rise to a faster search compared to its variant, binary search.
"""