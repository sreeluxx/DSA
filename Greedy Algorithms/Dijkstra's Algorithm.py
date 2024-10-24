import heapq

def dijkstra(graph, start):
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3},
    'E': {'C': 8, 'D': 3}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

for vertex, distance in shortest_paths.items():
    print(f"Shortest path from {start_vertex} to {vertex}: {distance}")
