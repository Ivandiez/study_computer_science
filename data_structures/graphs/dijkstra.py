import heapq


def dijkstra(graph, starting_vertex, ending_distance=None):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    if not ending_distance:
        return distances
    return distances.get(ending_distance, float("infinity"))


graph = {
    "A": {"B": 2, "C": 6},
    "B": {"D": 5},
    "C": {"D": 8},
    "D": {},
}

print(dijkstra(graph, "A"))  # {'A': 0, 'B': 2, 'C': 6, 'D': 7}
print(dijkstra(graph, "A", "D"))  # 7
