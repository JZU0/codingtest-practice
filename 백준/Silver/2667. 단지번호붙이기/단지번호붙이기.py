import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

home = [list(map(int, list(input().strip()))) for _ in range(N)]

result = []

def bfs (x, y):
    queue = deque([(x,y)])
    home[x][y] = -1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            cx, cy = x + dx, y + dy
            if (0<= cx < N and 0 <= cy < N and home[cx][cy]==1):
                home[cx][cy]=-1
                queue.append((cx,cy))
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if (home[i][j]==1):
            result.append(bfs(i,j))

print(len(result))
for r in sorted(result):
    print(r)