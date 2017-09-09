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

BST - 2 operations
------------------
- Insert operation - Insertion of a node in a BST takes O(h), where h is the height of the tree.

- Deleting nodes (removal of nodes) - The remove operation takes O(h), where h is the height of the tree

    3 scenarios, when the node that we want to remove has:
    -> No children => we simply detach it from its parent
    -> One child => the parent of that node is made to point to the child of that particular node
    -> Two children => find the next biggest descendant of node

BST - The minimum and maximum nodes - It takes O(h) to find the minimum/maximum value in a BST, h = height of the tree
-----------------------------------
- To find the node with smallest value: start our traversal from the root of the tree and visit the left node each time
we reach a sub-tree; To find the node with the biggest value in the tree do the opposite


Tree traversal - Visiting all the nodes in a tree/BST can be done:
--------------
 -  Depth-first traversal:
        -> In-order traversal (and infix notation): expression: (4 + 5) * (5 - 3)
        -> Pre-order traversal (and prefix notation = Polish notation PN; like LISP): * + 4 5 - 5 3
        -> Post-order traversal (and postfix notation = reverse Polish notation RPN): 4 5 + 5 3 - *
    follow a branch (or edge) to its limit before recoiling upwards to continue traversal; use recursive traversal

 - Breadth first traversal: starts from the root of a tree and visits the node from one level of the tree to the other

The breadth- & depth-first search traversal modes - implemented using queue recursion.

BST vs Linked list
------------------
Benefits: in most cases, finding data in a BST is faster than in a linked list
          although this is not the case if the data is inserted sequentially, unless the tree is balanced.

BST vs using a List for searching a term in a data set: e.g. 5, 3, 7, 1, 4, 6, and 9
- Using a list: the worst-case scenario: search through the entire list of 7 elements before finding the search term,
                Searching for 9 requires six jumps: 5-> 3, 3-> 7, 7-> 1, 1-> 4, 4-> 6, 6-> 9
- Using a tree: the worst-case scenario is 3 comparisons; Searching for 9 requires two steps: 5->7, 7->9

- However, if nodes are inserted into the tree in a sequential order: 1, 2, 3, 5, 6, 7, 9, then the tree behaves more
or less like a list <=> each node has exactly one child node
=> need of balancing the tree: reduce the height of the tree as much as possible, by filling up each row in the tree

Balancing trees - types:
---------------
- Self-balancing trees: red-black trees, AA trees, and scapegoat trees
   These balance the tree during each operation that modifies the tree, such as insert or delete.

- External algorithms: no need to balance the tree on every single operation, leave balancing to the point when need it
"""

from collections import deque


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

    # helper method to search for and return the node with its parent node
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return parent, None
        while True:
            if current.data == data:
                return parent, current
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

            return parent, current

    # Removal of a node - 3 scenarios
    def remove(self, data):
        # begin with the search
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        # Get children count
        children_count = 0
        if node.left_child and node.rigth_child:
            children_count = 2
        elif node.left_child is None and node.rigth_child is None:
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            # I. BST that has 1 node with 0 children
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None

        # II. node about to be deleted has 1 child
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.rigth_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        # III. the node about to be deleted has 2 children
        else:
            parent_of_leftmost_node = node
            # to find the in-order successor, move to the right node
            leftmost_node = node.rigth_child
            # as long as there exists a left node
            # When we get to the leftmost node, it will either be a leaf node (no child)/ have a right child
            while leftmost_node.left_child:
                parent_of_leftmost_node = node.rigth_child
                leftmost_node = node.left_child
            # update the node about to be removed with the value of the in-order successor
            node.data = leftmost_node.data

            #  attach the parent of the leftmost node with any child node
            # the in-order successor can only have a right child as its only child
            if parent_of_leftmost_node.left_child is leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self, data):
        #  start searching at the root
        current = self.root_node
        while True:
            # passed a leaf node, the data doesn't exist in the tree
            if current is None:
                return None
            # found the data
            elif current.data == data:
                return current
            # data we are searching for < data of the current node
            elif current.data > data:
                # go down the tree to the left
                current = current.right_child
            # data we are looking for > data held in the current node
            else:
                # go down the tree to the right
                current = current.left_child

    # Traversal: 2 ways:
    # I.Depth-first traversal - 3 ways:
    # I.1 In-order traversal: visit the left sub-tree, the parent node, and finally the right sub-tree
    # The recursive function to return an in-order listing of nodes in a tree
    def df_in_order_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        self.df_in_order_traversal(current.left_child)
        print(current.data)
        self.df_in_order_traversal(current.right_child)

    # I.2 Pre-order traversal: visit the node, the left sub-tree, and finally the right sub-tree node
    def df_pre_order_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.df_pre_order_traversal(current.left_child)
        self.df_pre_order_traversal(current.right_child)

    # I.3 Post-traversal: visit the left sub-tree, the right sub-tree, and lastly the root node
    def df_post_order_traversal(self, root_node):
        current = root_node
        if current is None:
            return
        self.df_post_order_traversal(current.left_child)
        self.df_post_order_traversal(current.right_child)
        print(current.data)

    # II. Breadth-first traversal - by using a queue data structure
    def bf_traversal(self):
        list_of_nodes = []
        # Starting with the root node, we push it into a queue
        # # The node at the front of the queue is accessed (dequeued) & printed/stored for later use
        traversal_queue = deque([self.root_node])

        # repeat as long as the queue is not empty
        while len(traversal_queue) > 0:
            #  The node at the front of the queue is popped off & appended to the list_of_nodes
            node = traversal_queue.popleft()
            list_of_nodes.append(node.data)

            # The left child node is added to the queue
            if node.left_child:
                traversal_queue.append(node.left_child)

            # The right child node is enqueued
            if node.rigth_child:
                traversal_queue.append(node.rigth_child)

        return list_of_nodes





tree = BST()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

for i in range(1, 10):
    found = tree.search(i)
    print('{} : {}'.format(i, found))



