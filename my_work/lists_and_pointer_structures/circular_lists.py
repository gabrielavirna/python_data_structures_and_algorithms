"""
Circular lists
---------------
- a special case of a linked list
- It is a list where the endpoints are connected: the last node in the list points back to the first node
- Circular lists can be based on both singly and doubly linked lists
- In the case of a doubly linked circular list, the first node also needs to point to the last node.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # make sure that the new node points back to the tail node
    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        # only this line added, compared to append method for class SingleLinkedList
        self.head.next = self.tail
        self.count += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        # this while changes, compared to 'while current:' for class SingleLinkedList
        # we cannot loop until current becomes None, since that will never happen
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    # make sure the head points to the tail
                    # this line added, compared to delete method for class SingleLinkedList
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
            return False


words = CircularSinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

words.delete('ham')

print(words.contains('ham'))
print(words.count)

# List traversal: need to put in an exit condition, otherwise program will get stuck in a loop
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 1000:
        break








