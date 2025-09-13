# Search min or max value will consume O(1) time
# Delete min or max value will consume O(logn) time
# Search consume O(n) time
# Insert consume O(logn) time

from heapq import heapify, heappop, heappush

a_list = ["R", "C", "T", "H", "E", "D", "L"]
heapify(a_list)  # Do minimal heap
print(a_list)  # ['C', 'E', 'D', 'H', 'R', 'T', 'L']

heappop(a_list)  # Pop the first (minimal) element and rebalance the heap
print("After popping:")
print(a_list)  # ['D', 'E', 'L', 'H', 'R', 'T']


new_list = ["D", "E", "L", "H", "R", "T"]
heapify(new_list)
while len(new_list) > 0:
    print(heappop(new_list))  # D E H L R T

another_list = ["D", "E", "L", "H", "R", "T"]
heappush(another_list, "Z")
print(another_list)  # ['D', 'E', 'L', 'H', 'R', 'T', 'Z']
