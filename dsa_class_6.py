##> w r
dsa_classs_6 = print


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        return "Stack is empty"
    else:
        return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return "stack is empty"
    else:
        return stack[-1]


stack = []

push(stack, "a")
push(stack, "b")
push(stack, "c")
push(stack, "d")
dsa_classs_6(stack)
dsa_classs_6("Top element", peek(stack))
dsa_classs_6("Pop", pop(stack))
dsa_classs_6(pop(stack))
dsa_classs_6(stack)


###Using class to create a stack
# Define the ArrayStack class
class ArrayStack:
    """
    Lifo stack implementation using a python list as underlying storage
    """

    def __init__(self):
        # create an empty stack
        self._data = []

    def __len__(self):
        # Return the number of elements in the stack
        return len(self._data)

    def is_empty(self):
        # Return True if the stack is empty
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            return self._data.pop()

# Create an object of ArrayStack
stack = ArrayStack()

# Push some elements onto the stack
stack.push(5)
print("Pushed 5 onto the stack. Stack:", stack._data)

stack.push(10)
print("Pushed 10 onto the stack. Stack:", stack._data)

# Print the top element of the stack
print("Top element of the stack:", stack.top())

# Pop an element from the stack
popped_element = stack.pop()
print("Popped element from the stack:", popped_element)
print("Stack after popping:", stack._data)


##Valid paenthesis
"""
20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def IsValidBracket(s):
    pair_parenthese = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for ch in s:
        if ch in pair_parenthese.keys():
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                peek_paparenthese = stack.pop()
                if pair_parenthese[peek_paparenthese] != ch:
                    return False

    if stack:
        return False
    else:
        return True


dsa_classs_6(IsValidBracket("()[]{}"))


