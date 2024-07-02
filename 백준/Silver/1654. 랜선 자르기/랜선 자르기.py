import sys
input = sys.stdin.readline

K, N= map(int, input().split())

arr = [int(input()) for _ in range(K)]

arr.sort()
start = 1
end = arr[-1]

while(start<=end):
    mid = (start + end) // 2
    cnt = 0
    loc = arr[0]
    for i in range(K):
        cnt += (arr[i] // mid)
    if cnt >= N:
        result = mid
        start = mid + 1
    elif cnt < N:
        end = mid -1
print(result)