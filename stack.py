class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

new_stack = Stack()

for i in range(0, 6):
    new_stack.push(i)

print(new_stack.peek())
print(new_stack.size())

# Test reverse string by stack
rev_stack = Stack()
for c in "Hello":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)