import sys

input = sys.stdin.readline

n = int(input().strip())

triangle = [list(map(int, input().strip().split())) for _ in range(n)]

result = 0

for i in range(1,n) :                          
    for j in range(0,i+1) :                  
        if j == 0 :
            triangle[i][0] += triangle[i-1][0]              
        elif j == i :
            triangle[i][j] += triangle[i-1][j-1]            
        else :
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])   

print(max(triangle[n-1]))  