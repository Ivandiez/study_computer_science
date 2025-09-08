class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Time complexity: O(1)
    def enqueue(self, item):
        self.s1.append(item)

    # Time complexity: O(n)
    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("pop from empty queue")
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        item = self.s2.pop()
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return item


q = Queue()
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
q.enqueue("e")
for i in range(4):
    print(q.dequeue())
