import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    queue = [(0,start)]
    distance = [INF] * (V+1)
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if (distance[node] < dist):
            continue
        for nextnode, nextdistance in graph[node]:
            if(dist + nextdistance < distance[nextnode]):
                distance[nextnode] = dist + nextdistance
                heapq.heappush(queue, (distance[nextnode],nextnode))

    return distance[end]
            
path1 = dijkstra(1,v1) + dijkstra(v1, v2) + dijkstra(v2,V)
path2 = dijkstra(1,v2) + dijkstra(v2, v1) + dijkstra(v1,V)

if(path1 >= INF and path2 >= INF):
    print(-1)
else:
    print(min(path1, path2))