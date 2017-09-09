"""
Stacks - LIFO data structure
----------------------------
- a data structure that is often likened to a stack of plates.
- If you have just washed a plate, you put it on top of the stack.
    => Add a plate to the stack: add it on top of the pile
    => Remove a plate from the stack: remove the plate that is on top of the pile.
- LIFO structure: the last plate to be added to the stack will be the first to be removed from the stack.

2 primary operations:
--------------------
- push: When an element is added to the top of the stack, it is pushed onto the stack
- pop: When an element is taken off the top of the stack, it is popped off the stack
- peek: makes it possible to see the element on the stack without popping it off


Usage
-----
-> stacks keep track of the return address during function calls.

def b():
    print('b')

def a():
    b()

a()
print("done")

When the program execution gets to the call to a(), it first pushes the address of the following instruction onto the
stack, then jumps to a. Inside a, b() is called, but before that, the return address is pushed onto the stack.
Once in b() and the function is done, the return address is popped off the stack, which takes us back to a().
When a has completed, the return address is popped off the stack, which takes us back to the print statement.

-> pass data between functions. Ex. following function call somewhere in your code:

   somefunc(14, 'eggs', 'ham', 'spam')

What is going to happen is that 14, 'eggs', 'ham' and 'spam' will be pushed onto the stack, one at a time.
When the code jumps into the function, the values for a, b, c, d will be popped off the stack.
The spam element will be popped off first and assigned to d, then "ham" will be assigned to c, and so on:

    def somefunc(a, b, c, d):
        print("function executed")
"""


class Node:
    def __init__(self, data=None):
        # a node holds data and a reference to the next item in a list
        self.data = data
        self.next = None


# Stack - like lists, same principle of nodes linked together
class Stack:
    def __init__(self):
        self.top = None # the node at the top of the stack
        self.size = 0

    # Push: used to add an element to the top of the stack
    def push(self, data):
        node = Node(data)
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





