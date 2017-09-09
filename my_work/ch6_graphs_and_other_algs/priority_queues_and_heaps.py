"""
Priority queues and heaps
--------------------------
A priority queue:
----------------
- is basically a type of queue that will always return items in order of priority.
- This priority could be that the lowest item is always popped off first.
Although it is called a queue, priority queues are often implemented using a heap - very efficient for this purpose.

E.g. in a store, customers queue in a line where service is only rendered at the front of the queue. Each customer will
spend some time in the queue to get served. If the waiting times for the customers in the queue are 4, 30, 2, and 1,
then the average time spent in the queue becomes (4 + 34 + 36 + 37)/4, which is 27.75. However, if we change the order
of service such that customers with the least amount of waiting time are served first, then we obtain a different
average waiting time. In doing so, we calculate our new average waiting time by (1 + 3 + 7 + 37)/4, which now equals 12,
a better average waiting time. Clearly, there is merit to serving the customers from the least waiting time upward.
This method of selecting the next item by priority or some other criterion is the basis for creating priority queues.

A heap:
------
- is a data structure that satisfies The Heap Property: there must be a certain relationship between a parent node and
its child nodes. This property must apply through the entire heap.

-> In a min heap: the parent must always be <= to its children => the lowest element in the heap must be the root node.
-> In a max heap, the parent is >= to its child/its children => the largest value makes up the root node.

- heaps are trees: binary trees.
- we will actually use a list to represent the binary tree; the heap will store a complete binary tree.
- A complete binary tree: a tree in in which each row must be fully filled before starting to fill the next row

- easy to retrieve the children of any node n: The left child is located at 2n and the right child is located at 2n + 1.
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

# creating our heap and inserting some data:
bh = BinaryHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
bh.build_heap(unsorted_list)
print(bh.heap)


# pop off the items, one at a time:
# Notice how the items come out in a sorted order, from lowest to highest.
# Also notice how the heap list changes after each pop.
print(bh.pop())
print(bh.heap)
print(bh.pop())
print(bh.heap)

