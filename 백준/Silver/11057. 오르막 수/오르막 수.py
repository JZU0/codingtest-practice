import sys

input = sys.stdin.readline

N = int(input())

arr = [[0]*10 for _ in range(N)]

for i in range(10):
    arr[0][i] = 1

for i in range(1,N):
    for j in range(10):
        total = 0
        for k in range(j,10):
            total += arr[i-1][k]
        arr[i][j] += total

print(sum(arr[N-1])%10007)