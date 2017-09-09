"""
Queue -  FIFO data structure
----------------------------
- Another special type of list; e.g. stay in line at an airport/ to be served your favorite burger at the shop

- a very fundamental and important concept to grasp since many other data structures are built on them.
- The way a queue works: the first person to join the queue usually gets served first, all things being equal.

- FIFO:  first in, first out  - E.g. people standing in a queue waiting for their turn to be served; service is only
rendered at the front of the queue; The only time people exit the queue - when they have been served (which occurs only
at the very front of the queue); it is illegal for people to join the queue at the front where people are being served.

To join the queue, participants must first move behind the last person in the queue - length of the queue doesn't matter

2 operations:
- enqueue: to add an element to the queue enqueue; anytime an element is enqueued, the length or size of the queue += 1
- dequeue: to remove an element from the queue; dequeuing items reduce the number of elements in the queue -= 1

"""

# I. List based queue


class ListBasedQueue:
    def __init__(self):
        # queue is empty when created
        self.items = []
        self.size = 0

    # Enqueue: inserts items/data at index 0 - 1st position
    # (could have used Python's shift method on the list as another way of implementing the "insert at 0")
    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    # Dequeue: removes items from the queue
    # capture the point where we serve the customer who joined the queue first and also waited the longest
    # pop - Removes the last item from the list & Returns the removed item from the list back to the user
    def dequeue(self):
        # The last item in the list is popped & saved in the data variable
        data = self.items.pop()
        self.size -= 1
        return data


# II. Stack-based queue - implementation of a queue using two stacks - interview question !!!!
class StackBasedQueue:
    def __init__(self):
        # 2 stacks = empty lists that allow us to call push and pop methods on them
        self.inbound_stack = [] # store elements that are added to the queue
        self.outbound_stack = []

    # enqueue: adds elements to the queue
    # append method used to mimic the push operation, which pushes elements to the top of the stack.
    def enqueue(self, data):
        self.inbound_stack.append(data)

    # dequeue
    def dequeue(self):
        # if the outbound_stack is empty, all the elements in the inbound_stack are moved to the outbound_stack
        if not self.outbound_stack:
            # as long as there are elements in the inbound_stack
            while self.inbound_stack:
                # self.inbound_stack.pop() will remove the latest element that was added to the inbound_stack
                # & immediately pass the popped data to the self.outbound_stack.append() method call.
                self.outbound_stack.append(self.inbound_stack.pop())
            # If not empty, remove the element at the front of the queue
        return self.outbound_stack.pop()


# III. Node-based queue - implementation by utilizing our knowledge of pointer structures, using a doubly linked list
# insertion and deletion operations on this data structure have a time complexity of O(1).
# The doubly linked list can be treated as a queue if it enables a FIFO data access: 1st element added, 1st to remove.

# uses the double-linked-list node
class Node:
    # The prev variable holds a reference to the previous node, the next variable holds a reference to the next node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class NodeBasedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # To count the number of nodes in Queue

    # enqueue: nodes are added to the queue - same append operation from doubly linked list
    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    # def dequeue: removes the node at the front of the queue
    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1


lqueue = ListBasedQueue()
lqueue.enqueue(1)
lqueue.enqueue(2)
lqueue.enqueue(3)
lqueue.enqueue(4)
for item in lqueue.items:
    print(item)
print('size of the queue is: {}'.format(lqueue.size),'\n')
lqueue.dequeue()
for item in lqueue.items:
    print(item)
print('size of the queue is: {}'.format(lqueue.size), '\n')

squeue = StackBasedQueue()
squeue.enqueue(5)
squeue.enqueue(6)
squeue.enqueue(7)
print(squeue.inbound_stack)
squeue.dequeue()
print(squeue.inbound_stack)
print(squeue.outbound_stack)
squeue.dequeue()
print(squeue.outbound_stack)