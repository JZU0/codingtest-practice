import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque([(0, 0, 0, 1)])
    visited[0][0][0] = True

    while queue:
        x, y, wall_broken, cnt = queue.popleft()

        if x == N - 1 and y == M - 1:
            return cnt

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    if not visited[nx][ny][wall_broken]:
                        visited[nx][ny][wall_broken] = True
                        queue.append((nx, ny, wall_broken, cnt + 1))
                elif arr[nx][ny] == 1 and wall_broken == 0:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, 1, cnt + 1))

    return -1

print(bfs())