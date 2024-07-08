import sys
input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

# R : 0, G : 1, B : 2

for i in range(1,N):
    for j in range(3):
        if(j==0):
            RGB[i][j] += min(RGB[i-1][1],RGB[i-1][2])
        elif(j==1):
            RGB[i][j] += min(RGB[i-1][0],RGB[i-1][2])
        else:
            RGB[i][j] += min(RGB[i-1][0],RGB[i-1][1])

print(min(RGB[N-1]))