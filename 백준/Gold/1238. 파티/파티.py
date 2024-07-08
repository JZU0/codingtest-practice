import heapq
import sys

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))

def dijkstra(start, graph):
    queue = [(0,start)]
    distance = [int(1e9)] * (N+1)
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if(distance[node] < dist):
            continue
        for nextnode, nextdistance in graph[node]:
            if(dist + nextdistance < distance[nextnode]):
                distance[nextnode] = dist + nextdistance
                heapq.heappush(queue, (distance[nextnode],nextnode))

    return distance
            
dist_from_X = dijkstra(X, graph)

dist_to_X = dijkstra(X, reverse_graph)

max_time = 0
for i in range(1, N+1):
    total_time = dist_from_X[i] + dist_to_X[i]
    if total_time > max_time:
        max_time = total_time

print(max_time)