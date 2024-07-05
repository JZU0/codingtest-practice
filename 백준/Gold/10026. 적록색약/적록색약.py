import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

color = [list(input().strip()) for _ in range(N)]

visited = set()

def bfs (x,y,blindness=False):
    flag = ""
    queue = deque([(x,y)])
    visited.add((x,y))
    while(queue):
        x, y = queue.popleft()
        flag = color[x][y]
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            cx, cy = x + dx, y + dy
            if(blindness):
                if flag=='B':
                    if(0<= cx < N and 0<= cy < N and color[cx][cy]=='B' and (cx,cy) not in visited):
                        visited.add((cx, cy))
                        queue.append((cx,cy))
                else:
                    if(0<= cx < N and 0<= cy < N and color[cx][cy]!='B' and (cx,cy) not in visited):
                        visited.add((cx, cy))
                        queue.append((cx,cy))
            else:
                if(0<= cx < N and 0<= cy < N and color[cx][cy]==flag and (cx,cy) not in visited):
                    visited.add((cx, cy))
                    queue.append((cx,cy))
                
    return 0

cnt = 0
blindness_cnt = 0
for i in range(N):
    for j in range(N):
        if (i,j) not in visited:
            bfs(i,j)
            cnt += 1

visited = set()
for i in range(N):
    for j in range(N):
        if (i,j) not in visited:
            bfs(i,j,True)
            blindness_cnt += 1

print(cnt,blindness_cnt)
