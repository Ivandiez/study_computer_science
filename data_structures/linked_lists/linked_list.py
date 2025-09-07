class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Time complexities for:
# Access: O(n)
# Search: O(n)
# Insertion: O(1)
# Deletion: O(1)
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def append_for_cycle(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return current.next

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def create_list(self, n, create_cycle=False):
        node = None
        for i in range(2, n):
            node = self.append_for_cycle(i)
        if create_cycle:
            if node:
                node.next = self.head

    def __str__(self):
        """To print elements of Linked List"""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return ""


a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)

# Test search
import random

b_list = LinkedList()

for i in range(20):
    j = random.randint(1, 30)
    b_list.append(j)
    print(j, end=" ")
print()
print(b_list.search(10))
print()


# Test remove
c_list = LinkedList()
for i in range(1, 10):
    c_list.append(i)
    print(i, end=" ")
print()
c_list.remove(1)
print(c_list)


# Test reverse
c_list.reverse_list()
print(c_list)


# Test detect cycle
print(c_list.detect_cycle())


# Built-in python `deque` - Double-ended queue
# uses linked list internally.
# We can use it instead of own class.
from collections import deque

d = deque()
d.append("Harry")
d.append("Ron")

print()
for item in d:
    print(item)


# Practice
t_list = LinkedList()
for i in range(1, 101):
    t_list.append(i)

print(t_list)


# Linked lists with and without cycles
ll_one = LinkedList()
ll_one.create_list(100)
ll_two = LinkedList()
ll_two.create_list(100, True)

print(ll_one.detect_cycle())
print(ll_two.detect_cycle())
