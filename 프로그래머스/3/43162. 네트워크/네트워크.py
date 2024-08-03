import sys
sys.setrecursionlimit(int(1e9))

def solution(n, computers):

    answer = 0
    visited = [False] * n

    def dfs(start):
        visited[start] = True
        for idx, c in enumerate(computers[start]):
            if c == 1 and not visited[idx]:
                dfs(idx)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer