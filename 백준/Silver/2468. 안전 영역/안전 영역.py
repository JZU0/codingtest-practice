import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

rain = []
value_max = 0

for _ in range(N):
    value = list(map(int, input().split()))
    rain.append(value)
    if(max(value) > value_max):
        value_max = max(value)

def bfs(start,limit):
    queue = deque([start])
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = cx + dx, cy + dy
            if (0<= nx <N and 0<= ny <N and rain[nx][ny] > limit and visited[nx][ny] == 0):
                queue.append((nx,ny))
                visited[nx][ny] = 1

result = []
for i in range(value_max):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if(rain[j][k] > i and visited[j][k] == 0):
                bfs((j,k),i)
                cnt += 1
    result.append(cnt)

print(max(result))