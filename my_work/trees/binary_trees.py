"""
Binary Trees
------------
- each node has a maximum of two children; no rules as to how elements are arranged in the tree
- used to build up a BST implementation

Binary search trees
-------------------
- BST : it is a tree that is structurally a binary tree;
- Functionally, it is a tree that stores its nodes in such a way to be able to search through the tree efficiently.
- Structure: For a given node with a value, all the nodes in the left sub-tree are <= the value of that node and
all the nodes in the right sub-tree > the parent node

2 operations
------------
- insert and remove operations - Insertion of a node in a BST takes O(h), where h is the height of the tree.

The minimum and maximum nodes - It takes O(h) to find the minimum/maximum value in a BST, h = the height of the tree
-----------------------------
- To find the node with smallest value: start our traversal from the root of the tree and visit the left node each time
we reach a sub-tree; To find the node with the biggest value in the tree do the opposite
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class BST:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        # The while loop continues to get the left node
        # and visits it until the last left node points to None
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current:
            current = current.right_child
        return current

    # For each given node, its left child node will hold data <= its own value
    # That node's right child node will hold data > data of its parent node
    # add data as nodes to the BST
    def insert(self, data):
        new_node = Node(data)

        if self.root_node is None:
            #  the new node becomes the root node
            self.root_node = new_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current

                if new_node.data < current.data:
                    # check whether the current node has a left child node
                    current = current.left_child
                    # if it doesn't, this is where we insert the new node
                    if current is None:
                        parent.left_child = new_node
                        return
                # node.data >= current.data
                else:
                    # check whether the current node has a left child node
                    current = current.right_child
                    if current is None:
                        # If it doesn't, the new node is inserted as the right child node
                        parent.right_child = new_node
                        return






