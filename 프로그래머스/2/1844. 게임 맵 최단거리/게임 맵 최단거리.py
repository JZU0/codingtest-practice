from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    answer = 0
    visited = [[False]*(n) for _ in range(m)]
    def bfs():
        queue = deque([(0,0,1)])
        visited[0][0] = True
        while queue:
            x, y, cnt = queue.popleft()
            if(x == m-1 and y == n-1):
                return cnt
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                cx, cy = x + dx, y + dy
                if(0<=cx<m and 0<=cy<n and maps[cx][cy]==1 and visited[cx][cy]==False):
                    queue.append((cx,cy,cnt+1))
                    visited[cx][cy] = True
    answer = bfs()
    if not answer:
        return -1
    else:
        return answer