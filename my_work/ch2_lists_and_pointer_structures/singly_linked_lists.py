"""
Singly linked lists
-------------------
- is a list with only 1 pointer between 2 successive nodes
- It can only be traversed in a single direction: from the 1st node in the list to the last node


Several problems
----------------
It requires too much manual work by the programmer
It is too error-prone (this is a consequence of the first point)
Too much of the inner workings of the list is exposed to the programmer
"""

"""Singly linked list implementation"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


n1 = Node("eggs")
n2 = Node("spam")
n3 = Node("ham")

# Link the nodes together so that they form a chain
n1.next = n2
n2.next = n3

# To traverse the list: start by setting the variable current to the first item in the list:
# Loop: print the current element; set current to point to the next element in the list; until reaching the end of list

current = n1
while current:
    print(current.data)
    current = current.next

print("\n")

"""
Singly linked list class
-------------------------
Create a very simple class to hold our list. Start with a constructor that holds a reference to the very first node in 
the list. Since this list is initially empty, start by setting this reference to None:

Append 
-------
- append items to the list(insert operation):
- hide away the Node class. The user of our list class should really never have to interact with Node objects.
- Big problem: it has to traverse the entire list to find the insertion point => Ok few items in the list, but not to 
add thousands of items. Each append will be slightly slower than the previous one 
- Worst case running time of the append operation: O(n) 

Faster append operation
--------------------------
- store, not only a reference to the first node in the list, but also a reference to the last node. 
- Make sure the previous last node points to the new node, that is about to be appended to the list.
=> quickly append a new node at the end of the list. 
- Reduced worst case running time: O(1). 

Size of the list
-----------------
- counting the number of nodes: traverse the entire list and increase a counter as we go along
- works but list traversal is potentially an expensive operation that we should avoid 
- Worst case running time: O(n) because of using a loop to count the number of nodes in the list

Better size of the list
-----------------------
- add a size member to the SinglyLinkedList class, initializing it to 0 in the constructor. 
- Then increment size by one in the append method
- Reduced the worst case running time: O(1), because we are now only reading the size attribute of the node object


Improving list traversal
-------------------------
Still exposed to the Node class; need to use node.data to get the contents of the node and node.next to get next node. 
But client code should never need to interact with Node objects => Create a method that returns a generator: iter()


Deleting nodes
--------------
Decide how to select a node for deletion: by an index number/ by the data the node contains? Here delete by the data
- to delete a node that is between 2 other nodes, make the previous node directly to the successor of its next node
-  O(n) to delete a node 

List search
------------
- check whether a list contains an item.
- each pass of the loop compares the current data to the data being searched for; if match: True returned, else: False


Clear a list
 ------------
Clear the pointers head and tail by setting them to None
By orphaning all the nodes at the tail and head pointers of the list => effect of orphaning all the nodes in between
"""


class SinglyLinkedListSlow:
    def __init__(self):
        self.tail = None

    # Worst case running time: O(n)
    def append(self, data):
        # encapsulate data in a Node
        # so that it now has the next pointer attribute
        node = Node(data)

        # check if there are any existing nodes in the list
        # does self.tail point to a Node ?
        if self.tail is None:
            # if none, make the new node the first node of the list
            self.tail = node
        else:
            # find the insertion point by traversing the list to the last node
            # updating the next pointer of the last node to the new node.
            current = self.tail
            while current.next:
                current = current.next
            current.next = node

    # Worst case running time: O(n)
    def size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count


#############################################################################


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # to compute size of list

    # Worst case running time: O(1)
    # append new nodes through self.head
    # the self.tail variable points to the first node in the list
    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1  # worst case running time: O(1)

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

            # Traverse the list - iter() method yields the data member of the node

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def search(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False

    # clear the entire list
    def clear(self):
        self.tail = None
        self.head = None


# append a few items
words1 = SinglyLinkedListSlow()
words1.append('egg')
words1.append('ham')
words1.append('spam')

# append faster
words2 = SinglyLinkedList()
words2.append('egg')
words2.append('ham')
words2.append('spam')

# List traversal
current = words1.tail
while current:
    print(current.data)
    current = current.next
print("\n")

# List traversal using iter
for word in words2.iter():
    print(word)
print("\n")

# Size of list
print(words1.size())
print(words2.size)
print("\n")

# Delete a node
words2.delete('ham')
for word in words2.iter():
    print(word)
print(words2.size)
print('\n')

# Search for a node
print(words2.search('spam'))
