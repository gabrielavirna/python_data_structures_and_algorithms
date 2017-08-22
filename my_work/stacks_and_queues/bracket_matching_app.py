"""
Bracket-matching application
----------------------------
- using our stack implementation, verify whether a statement containing brackets --(, [, or {-- is balanced:
    whether the number of closing brackets matches the number of opening brackets
- It will also ensure that one pair of brackets really is contained in another

Run Time Complexity: O(1) - the push and pop operations of the stack data structure
The stack data structure usage: The back & forward buttons on the browser; undo & redo functionality in word processors
"""

from projects.python_data_structures_algorithms.my_work.stacks_and_queues.stack import Node, Stack


def check_balanced_brackets(statement):
    stack = Stack()
    # parses each character in the statement passed to it
    for ch in statement:
        # If it gets an open bracket, it pushes it onto the stack
        if ch in ('{', '[', '('):
            stack.push(ch)
            # If it gets a closing bracket, it pops the top element off the stack
        if ch in ('}', ']', ')'):
            last = stack.pop()
            # and compares the two brackets to make sure their types match: (), [], {}
            if last is '{' and ch is '}':
                # continue parsing
                continue
            elif last is '[' and ch is ']':
                continue
            elif last is '(' and ch is ')':
                continue
            else:
                return False

    if stack.size > 0:
        # if the stack is not empty, then we have some opening bracket which does not have a matching closing bracket
        return False
    else:
        return True


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in sl:
    m = check_balanced_brackets(s)
    print("{}: {}".format(s, m))
