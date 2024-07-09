import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in map(int, input().split()):
    arr.append(i)

start, end = 0, N-1

min_val = float('inf')

while start < end:
    total = abs(arr[start] + arr[end])
    if total < min_val:
        min_val = total
        answer = [arr[start], arr[end]]

    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1
print(*answer)