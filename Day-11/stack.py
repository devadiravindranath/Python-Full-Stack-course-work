"""#stack operation 
stack=[]
stack.append(10)
stack.append(11)
stack.append(15)
stack.append(16)
stack.append(12)
stack.append(17)
stack.append(18)
stack.append(14)
print("stack after pushing: ",stack)
deleted =stack.pop()
print("stack after popping: ",stack)
deleted = stack.pop()
print("stack after popping 2 times: " ,stack)

print("stack element ready to be popped : ",stack[-1])
print("remaining size of the stack: ",len(stack))"""

#write a code to write user defined input to create a stack
"""stack=[]
n=int(input("Enter the size of stack: "))
for i in range(n):
    value=int(input("enter a value: "))
    stack.append(value)
print("stack:",stack)
print("pop:",stack.pop())
print("stack:",stack)"""


#write a code to create a stack using a class and access the elements in the stack

class stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack)==0:
            return "stack Empty........"
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "stack Empty........"
        return self.stack[-1]
    def display(self):
        return self.stack
s=stack()
s.push(2)
s.push(22)
s.push(222)
s.push(2222)
print("stack: ",s.display())
print("pop: ",s.pop())
print("peek: ",s.peek())




























