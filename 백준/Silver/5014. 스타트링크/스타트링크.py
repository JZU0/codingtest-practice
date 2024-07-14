import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
vistied = [0]*(F+1)

def dfs(f,s,g,u,d):
    queue = deque([s])
    while queue:
        curr = queue.popleft() 
        vistied[curr] += 1
        if(curr == g):
            print(vistied[curr]-1)
            exit()
        for i in ["up","down"]:
            if(i=='up'):
                after = curr + u
            else:
                after = curr - d    
            if(1 <= after and after <= f and not vistied[after]):
                queue.append(after)
                vistied[after] += vistied[curr]

dfs(F, S, G, U, D)
print("use the stairs")