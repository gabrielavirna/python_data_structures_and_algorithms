"""
Expression trees
----------------
- The tree structure is also used to parse arithmetic and Boolean expressions
E.g. - the expression tree for 3 + 4, (4 + 5) * (5-3)

Parsing a reverse Polish expression
-----------------------------------
- use a simple tree implementation for the expression written in postfix notation: 4 5 + 5 3 - *
"""


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.next = None


# Stack - like lists, same principle of nodes linked together
class Stack:
    def __init__(self):
        self.top = None  # the node at the top of the stack
        self.size = 0

    # Push: used to add an element to the top of the stack
    def push(self, data):
        node = TreeNode(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    # Pop: removes the top element from the stack
    # Need to return the topmost element as well; return None if there are no more elements
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            # If the top node has its next attribute pointing to another node
            if self.top.next:
                # must set the top of the stack to now point to that node
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    # Peek: If there is a top element, return its data, without removing it from the stack
    def peek(self):
        if self.top:
            data = self.top.data
            return data
        else:
            return None


# I. Build the expression tree to represent an arithmetic expression

# use a stack to parse an expression written in RPN
# create an arithmetic expression and set up our stack:
expr = "4 5 + 5 3 - *".split()  # expr = a list with the values 4, 5, +, 5, 3, - and *.
stack = Stack()

# Each element of the expr list is an operator/an operand
for term in expr:
    # If operator, embed it into a tree node & pop its two operands into the node's left and right children
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()  # 1st pop into the right child, otherwise => problems with subtraction & division
        node.left = stack.pop()
    # If operand, embed it in a tree node & push it onto the stack
    else:
        node = TreeNode(int(term))  # or float()
    stack.push(node)


# II. Evaluate the expression
def calc(node):
    # If node contains an operator, perform the operation that it represents, on the node's 2 children
    #  since one/more of the children could also contain operators/operands, call the calc() function recursively
    if node.data is "+":
        return calc(node.left) + calc(node.right)
    elif node.data is "-":
        return calc(node.left) - calc(node.right)
    elif node.data is "*":
        return calc(node.left) * calc(node.right)
    elif node.data is "/":
        return calc(node.left) / calc(node.right)
    # If the node contains an operand, simply return that value
    else:
        return node.data


# The result of the calculation: pop the root node off the stack and pass it into the calc() function
root = stack.pop()
result = calc(root)
print(result)  # prints 18, the result of (4 + 5) * (5 - 3)
