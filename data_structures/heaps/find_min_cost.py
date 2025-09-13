from heapq import heapify, heappop, heappush


def find_min_cost(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)
        heappush(ropes, sum)
        cost += sum
    return cost


ropes = [5, 4, 2, 8]
print(find_min_cost(ropes))
