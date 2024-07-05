import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

queue = deque([]) 

def bfs ():
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            cx, cy = x + dx, y + dy
            if (0<= cx < N and 0<= cy < M and tomato[cx][cy]==0):
                tomato[cx][cy] = tomato[x][y] + 1
                queue.append((cx,cy))          
    return 0

flag = True

for row in tomato:
    if 0 in row:
        flag = False

if flag == True:
    print(0)
    exit()
else:
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i,j))
    bfs()
                

day = 0
for i in range(N):
    for j in range(M):
        if(tomato[i][j]==0):
            print(-1)
            exit()
        day = max(day, max(tomato[i]))

print(day-1)