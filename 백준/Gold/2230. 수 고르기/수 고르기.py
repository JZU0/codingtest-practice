import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [int(input().strip()) for _ in range(N)]

arr.sort()

start = 0
end = 0
gap = 0
result = []

while True:
    gap = abs(arr[end]-arr[start])
    if gap >= M:
        start += 1
        result.append(gap)
    elif gap == M:
        break
    else:
        end += 1
    if(end > N-1 or start > end):
        break

print(min(result))