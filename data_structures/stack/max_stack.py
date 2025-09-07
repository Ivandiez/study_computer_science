class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n > self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]


max_stack = MaxStack()
max_stack.push(10)
print(max_stack.main)
print(max_stack.max)

max_stack.push(15)
print(max_stack.main)
print(max_stack.max)
print(max_stack.get_max())

max_stack.pop()
print(max_stack.main)
print(max_stack.max)
print(max_stack.get_max())

max_stack.pop()
print(max_stack.main)
print(max_stack.max)
