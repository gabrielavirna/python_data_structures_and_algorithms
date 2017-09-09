"""
Heap sort
---------
- implementation uses the heap data structure (-> implemented in In Chapter 6, Graphs and Other Algorithms)
- Implementation always made sure that after an element has been removed or added to a heap, the heap order property
is maintained by using the sink and float helper methods.

Worst case runtime
------------------
The for loop simply calls the pop method self.size number of times. The insert method is called n number of times.
Together with the float method, the insert operation takes a worst case runtime of O(n log n), as does the pop method.
=> this sorting algorithm worst case runtime: O(n log n).
"""


# I. Min Heap implementation
class BinaryHeap:
    def __init__(self):
        # initialize the heap list with a zero to represent the dummy 1st element
        self.heap = [0]
        # size of the heap
        self.size = 0

    # to reorganize the heap
    # loop until the root node (index 1) is reached so that we can keep floating the element
    # up as high as it needs to go as soon as we get below 2, the loop will break out:
    def float(self, k):
        while k // 2 == 0:
            # Compare,if the child < than the parent, swap the 2 values:
            if self.heap[k] < self.heap[k // 2]:
                temp = self.heap[k]
                self.heap[k] = self.heap[k // 2]
                self.heap[k // 2] = temp

            # move up the tree:
            k //= 2

    # Inserting method - called n number of times.
    # add the new element to the end of the list (the bottom of the tree) and increase the size of the heap by one
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        # after each insert, we need to float the new element up if needed.
        # the lowest element in the min heap needs to be the root element.
        self.float(self.size)

    # determine which of the children to compare our parent node against.
    def min_child_index(self, k):
        # if we get beyond the end of the list, return the index of the left child:
        if k * 2 + 1 > self.size:
            return k * 2
        # Otherwise, return the index of the lesser of the 2 children:
        else:
            if self.heap[k * 2] < self.heap[k * 2 + 1]:
                return k * 2
            else:
                return k * 2 + 1

    # to determine where to sink the element down: We compare the 2 children
    # the lowest element will be the one to float up as the root sinks down:
    def sink(self, k):
        # loop so that we can sink our element down as far as is needed:
        while k * 2 <= self.size:
            # need to know which of the left or the right child to compare against
            mi = self.min_child_index(k)

            # Compare,if the parent > than the child, swap the 2 values:
            if self.heap[k] > self.heap[mi]:
                temp = self.heap[k]
                self.heap[k] = self.heap[mi]
                self.heap[mi] = temp

            # move down the tree so that we don't get stuck in a loop:
            k = mi

    # Pop
    # remove the root node and decrement the size of the heap by one.
    # the root has been popped off => need a new root node: the last item in the list <=>
    # move it to the beginning of the list; But now we might not have the lowest element at the top of the heap
    # => let the new root node sink down as required
    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def build_heap(self, a_list):
        k = len(a_list) // 2
        self.size = len(a_list)
        self.heap = [0] + a_list[:]
        while k > 0:
            self.sink(k)
            k -= 1

    # The for loop simply calls the pop method self.size number of times.
    # sorted_list will contain a sorted list of items after the loop terminates.
    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
            return sorted_list


bh = BinaryHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
bh.build_heap(unsorted_list)
print(bh.heap)
bh.pop()
print(bh.heap)
bh.heap_sort()
print(bh.heap)
