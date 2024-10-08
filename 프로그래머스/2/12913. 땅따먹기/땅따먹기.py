def solution(land):
    n = len(land)
    temp = [[0]*4 for _ in range(n+1)]
    for i in range(0,n):
        for j in [0,1,2,3]:
            if(j==0):
                temp[i][j] = land[i][j] + max(temp[i-1][1],temp[i-1][2],temp[i-1][3])
            elif(j==1):
                temp[i][j] = land[i][j] + max(temp[i-1][0],temp[i-1][2],temp[i-1][3])
            elif(j==2):
                temp[i][j] = land[i][j] + max(temp[i-1][0],temp[i-1][1],temp[i-1][3])
            elif(j==3):
                temp[i][j] = land[i][j] + max(temp[i-1][0],temp[i-1][1],temp[i-1][2]) 
    return max(temp[n-1])