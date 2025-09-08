from queue import Queue

q = Queue()
q.put("a")
q.put("b")
q.put("c")
print(q.qsize())
for i in range(3):
    print(q.get())
