"""
Doubly linked list
------------------
In a Singly linked list, there exists one link between each successive node.
A node in a doubly linked list has two pointers: a pointer to the next node and a pointer to the previous node.

Singly linked list:
- a node can only determine the next node associated with it. But the referenced node or next node
- has no way of telling who is doing the referencing; the flow of direction is only one way
- Because a Singly linked list can only be traversed in one direction it may sometimes mean moving to the start or
beginning of the list in order to effect certain changes buried within the list.

Doubly linked list:
- reference both the next node & the previous node, 2 pointers that point to the next and previous nodes
- can be traversed in any direction. Depending on the operation being performed, a node within a doubly linked list can
- easily refer to its previous node where necessary without having to designate a variable to keep track of that node.
- immediate access to both next and previous nodes => deletion operations are much easier to perform


Append
------
- check whether the head is None
- If None, it means that the list is empty and should have the head set pointing to the just-created node
- The tail is also pointed at the new node through the head; head and tail will now be pointing to the same node:"""

"""A doubly linked list node"""


class Node:
    # The prev variable holds a reference to the previous node, the next variable holds a reference to the next node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""Doubly linked list class"""


class DoublyLinkedList:
    # convention: self.head points to the beginner node of the list & self.tail points to the latest node added to list.
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0  # to compute size of the list

    # O(1) for the append operation
    def append(self, data):
        new_node = Node(data, None, None)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            # The new node's previous variable is set to the tail of the list
            new_node.prev = self.tail
            # The tail's next pointer (or variable) is set to the new node
            self.tail.next = new_node
            # Lastly, we update the tail pointer to point to the new node
            self.tail = new_node

            # append operation increases the number of nodes by one
        self.count += 1

    # O(n) for the delete operation
    # 4 scenarios before deletion of a node
    def delete(self, data):
        # the current variable is set to the head of the list: it points to self.head
        current = self.head
        node_deleted = False

        # I. When the search item is not found at all
        # head node is searched first; if None => the list has no nodes => nothing to delete
        if current is None:
            node_deleted = False

        # II. When the search item is found at the very beginning of the list
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        # III. When the search item is found at the tail end of the list
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        # IV. When the search item is found somewhere in the middle of the list
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    # Traverse the list - iter() method yields the data member of the node
    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    # List search
    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False


words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# List traversal using iter
for word in words.iter():
    print(word)

words.delete('ham')

print(words.contains('ham'))

print(words.count)