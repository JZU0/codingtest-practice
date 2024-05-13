from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, x, y):
    queue = deque([(x,y)])
    graph[x][y] = -1
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx + dx, cy + dy
            if(0 <= nx < n and 0 <= ny < m and graph[nx][ny]==1):
                queue.append((nx,ny))
                graph[nx][ny] = -1
                count += 1
    return count

result = []

for i in range(n):
    for j in range(m):
        if(graph[i][j]==1):
            result.append(bfs(graph,i,j))
        
print(len(result))
if(len(result)):
    print(max(result))
else:
    print(0)