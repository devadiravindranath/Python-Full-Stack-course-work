#write a code to reverse of a string using a stack
"""
text=input("enter a String: ")
stack=[]
for ch in text:
    stack.append(ch)
rev_string=""
while stack:
    rev_string+=stack.pop()
print("reversed string: ",rev_string)
"""
#write a code to check an expression to balance

"""exp=input("Enter an expression: ")
stack=[]
balanced = True
for ch in exp:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack:
            balnced = False
            break
if balanced and not stack:
    print("balanced")
else:
    print("not")"""

#write a code to perform stack empty in a stack
"""
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            print("Stack empty!!!!")
        else:
            print("Popped:", self.stack.pop())


s = Stack()
s.pop()
"""

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def is_full(self):
        return len(self.stack) == self.size

    def push(self, value):
        if self.is_full():
            print("Stack overflow!!!!")
        else:
            self.stack.append(value)
            print(value, "pushed")


s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)













