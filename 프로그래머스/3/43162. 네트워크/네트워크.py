import sys
sys.setrecursionlimit(int(1e9))

def solution(n, computers): 
    
    tmp = []
    answer = 0
    
    def dfs(start,cnt=0):
        computers[start][start] = 0
        for idx, c in enumerate(computers[start]):
            if(c==1):
                computers[start][idx] = 0
                dfs(idx)
            
    for i in range(n):
        for j in range(n):
            if(computers[i][j]==1):
                dfs(i)
                answer += 1

    return answer