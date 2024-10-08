def solution(land):
    n = len(land)
    temp = [[0]*4 for _ in range(n)]

    for i in range(n):
        for j in range(4):
            temp[i][j] = land[i][j] + max(temp[i-1][k] for k in range(4) if k != j)

    return max(temp[n-1])