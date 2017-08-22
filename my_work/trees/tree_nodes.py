"""
 Trees
------
-  built up of nodes; the nodes that make up a tree need to contain data about the parent-child relationship
"""


# a node is a container for data and holds references to other nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


n1 = Node("root")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

# connect the nodes to each other: let n1 be the root node with n2 and n3 as its children, n4 as the left child to n2
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


# traverse the tree structure: traverse the left sub-tree
def traverse():
    current = n1
    # until we have reached the end of the left sub-tree:
    while current:
        # print out the node
        print(current.data)
        # move down the tree to the next left node
        current = current.left_child

