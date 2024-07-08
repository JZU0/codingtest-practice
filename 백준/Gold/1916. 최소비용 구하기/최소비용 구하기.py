import sys
input = sys.stdin.readline

INF = int(1e10)

N = int(input())
M = int(input())

graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

start, end = map(int, input().split())

def dijkstra(start):
    distance = {i: INF for i in range(1, N + 1)}
    visited = {i: False for i in range(1, N + 1)}

    distance[start] = 0

    for _ in range(N):
        min_distance = INF
        min_node = None
        for node in range(1, N + 1):
            if not visited[node] and distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node

        if min_node is None:
            break

        visited[min_node] = True

        for neighbor, weight in graph[min_node].items():
            if distance[min_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[min_node] + weight

    return distance

distance = dijkstra(start)

print(distance[end])