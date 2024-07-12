import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

n = int(input())

start, end = map(int, input().split())

m = int(input())

vistied = [False] * (n+1)
arr = {}
result = []

for _ in range(m):
    x, y = map(int, input().split())
    if x not in arr:
        arr[x] = [y]
    else:
        arr[x].append(y)
    if y not in arr:
        arr[y] = [x]
    else:
        arr[y].append(x)

def dfs(start, cnt):
    cnt += 1
    vistied[start] = True

    if(start == end):
        result.append(cnt)
    
    for node in arr[start]:
        if not vistied[node]:
            dfs(node, cnt)

dfs(start, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)