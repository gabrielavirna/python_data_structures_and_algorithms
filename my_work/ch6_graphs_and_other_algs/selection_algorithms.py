"""
Selection algorithms
--------------------
- under a class of algorithms that seek to answer the problem of finding the ith-smallest element in a list.

When a list is sorted in ascending order, the first element in the list will be the smallest item in the list.
The second element in the list will be the second-smallest element in the list. The last element in the list
will be the last-smallest element in the list but that will also qualify as the largest element in the list.

In creating the heap data structure, we have come to the understanding that a call to the pop method will return
the smallest element in the heap. The first element to pop off a min heap is the first-smallest element in the list.
Similarly, the seventh element to be popped off the min heap will be the seventh-smallest element in the list.
Therefore, to find the ith-smallest element in a list will require us to pop the heap i number of times.
That is a very simple and efficient way of finding the ith-smallest element in a list.

But in Chapter 11, Selection Algorithms, we will study another approach to find the ith-smallest element in a list.

Selection algorithms have applications in filtering out noisy data, finding the median, smallest, and largest elements
in a list, and can even be applied in computer chess programs.
"""