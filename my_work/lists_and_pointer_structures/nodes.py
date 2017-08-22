"""
A node
------
- a container of data, together with one or more links to other nodes. A link is a pointer.

a = "eggs"
b = "ham"

 The string is not really stored in the node, but is rather a pointer to the actual string.
 The storage requirement for this simple node is 2 memory addresses.
 The data attribute of the nodes are pointers to the strings eggs and ham.


Types of nodes:
--------------
- a simple node: one that only has a link to the next node
3 nodes: eggs, ham, spam.
eggs node points to the ham node, ham node points to the spam nod: eggs.next = ham, ham.next = spam, spam.next = None
=> Endpoints: Last node in the chain of nodes has its next point pointing to None.


- To go from A to B, but also from B to A:  add a previous pointer in addition to the next pointer:
A.next = B, B.next = None, B.previous = A, A.previous = None

"""

""" Node implementation """
#  the next pointer is initialized to None, so unless you change the value of next, the node is going to be an end-point


class Node:
    def __init__(self, data=None):
        # a node holds data and a reference to the next item in a list
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

