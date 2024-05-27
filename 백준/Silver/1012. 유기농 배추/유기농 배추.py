import sys
from collections import deque

T = int(sys.stdin.readline().strip())

def bfs(graph, x, y):
    queue = deque([(x,y)])
    graph[x][y] = -1
    count = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0),(-1,0),(0,1),(0,-1)]:
            nx, ny = cx + dx, cy + dy
            if(0 <= nx < M and 0 <= ny < N and graph[nx][ny]==1):
                queue.append((nx,ny))
                graph[nx][ny] = -1
                count += 1
    return count

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    result = []

    for i in range(M):
        for j in range(N):
            if(graph[i][j]==1):
                result.append(bfs(graph,i,j))
        
    print(len(result))
