"""
Sorting
-------
Whenever data is collected, there comes a time when it becomes necessary to sort the data.
The sorting operation is common to all datasets: a collection of names, telephone numbers, items on a simple to-do list.

Sorting techniques
------------------

Bubble sort     - simplest
Insertion sort
Selection sort
Quick sort
Heap sort

Quick sort performs much better than the other sorting algorithms. Of these algorithms, quick sort preserves the index
of the list that it sorts => use this property in chapter selection algorithms.

In our treatment of these sorting algorithms, we will take into consideration their asymptotic behavior.
Some of the algorithms are relatively easy to develop but may perform poorly.
Other algorithms that are a little complex to write will show impressive performance.

After sorting, it becomes much easier to conduct search operations on a collection of items.

Sorting algorithms
------------------
- they have varying levels of difficulty of implementation.

-> categorized by their memory usage, complexity, recursion, whether they're comparison-based among other considerations.
- Some of the algorithms use more CPU cycles and as such have bad asymptotic values.
- Others chew on more memory and other computing resources as they sort a number of values.

-> Another consideration is how sorting algorithms lend themselves to being expressed recursively/iteratively or both.
- There are algorithms that use comparison as the basis for sorting elements: bubble sort algorithm.
- Examples of a non-comparison sorting algorithm: the buck sort and pigeonhole sort.
"""