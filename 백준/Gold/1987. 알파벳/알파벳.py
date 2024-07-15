import sys

input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

ans = 0
visited = set()
checked = [[0] * C for _ in range(R)]

def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        cx, cy = x + dx, y + dy
        if ( 0 <= cx < R and 0 <= cy < C and arr[cx][cy] not in visited):
            visited.add(arr[cx][cy])
            dfs(cx, cy, cnt+1)
            visited.remove(arr[cx][cy])
    
visited.add(arr[0][0])
dfs(0,0,1)
print(ans)
 
# def bfs(x,y,r,c,max_value=-1):
#     queue = deque([(x,y)])
#     visited.add(arr[x][y])
#     checked[x][y] = 1
#     while queue:
#         x, y = queue.popleft()
#         max_value = max(max_value, checked[x][y])
#         for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#             cx, cy = x + dx, y + dy
#             if ( 0 <= cx < r and 0 <= cy < c and arr[cx][cy] not in visited):
#                 queue.append((cx,cy))
#                 visited.add(arr[cx][cy])
#                 checked[cx][cy] = checked[x][y] + 1
#         print(checked)
#     return max_value

# print(bfs(0,0,R,C))