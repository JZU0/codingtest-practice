from collections import deque

N, M, V= map(int, input().split())

graph = {}
ans_bfs = [V]
visited = set()
ans_dfs = []

for _ in range(M):
    k, val = map(int, input().split())
    if k not in graph:
        graph[k] = []
    if val not in graph:
        graph[val] = []    
    graph[k].append(val)
    graph[val].append(k)
    graph[k].sort()
    graph[val].sort()

def dfs(curr_node, graph, visited):
    visited.add(curr_node)
    ans_dfs.append(curr_node)
    for next_node in graph.get(curr_node, []):
        if next_node not in visited:
            dfs(next_node, graph, visited)
    return visited
                                                                                             
def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        curr_node = queue.popleft()

        for next_node in graph.get(curr_node, []):
            if next_node not in visited:
                visited.add(next_node)
                ans_bfs.append(next_node)
                queue.append(next_node)
    return -1

dfs(V, graph, visited)
bfs(graph, V)

print(*ans_dfs)
print(*ans_bfs)
