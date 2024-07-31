def solution(k, dungeons):
    max_count = 0
    
    def backtrack(k, dungeons, visited, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                backtrack(k - dungeons[i][1], dungeons, visited, count + 1)
                visited[i] = False

    visited = [False] * len(dungeons)
    backtrack(k, dungeons, visited, 0)
    
    return max_count