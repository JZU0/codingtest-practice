import sys

computer = int(sys.stdin.readline().strip())
pair = int(sys.stdin.readline().strip())

graph = [[] for i in range(computer+1)] 
visited=[0]*(computer+1)
for i in range(pair): 
    a,b = map(int, sys.stdin.readline().split())
    graph[a]+=[b] 
    graph[b]+=[a] 

def dfs(v):
    visited[v] = 1
    for c in graph[v]:
        if(visited[c]==0):
            dfs(c)

dfs(1)
print(sum(visited)-1)