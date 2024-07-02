import sys
input = sys.stdin.readline

N, C = map(int, input().split())

arr = [int(input()) for _ in range(N)]

arr.sort()
start = 1
end = arr[-1]-arr[0]

if C == 2:
    print(end)
else:
    while(start<=end):
        mid = (start + end) // 2
        cnt = 1
        loc = arr[0]
        for i in range(N):
            if(arr[i]-loc) >= mid:
                cnt+=1
                loc = arr[i]
        if cnt >= C:
            result = mid
            start = mid + 1
        elif cnt < C:
            end = mid -1
    print(result)