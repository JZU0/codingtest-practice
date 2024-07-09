import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start, graph):
    queue = [(0,start)]
    distance = [int(1e9)] * (V+1)
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
            
result = dijkstra(start, graph)
for i in range(1, V+1):
    if(result[i]==int(1e9)):
        print("INF")
    else:
        print(result[i])