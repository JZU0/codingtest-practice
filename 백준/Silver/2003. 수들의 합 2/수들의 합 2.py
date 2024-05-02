N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0
ans = 0
hap = 0

while(True):
    if(hap < M):
        if(end == N):
            break
        hap += A[end]
        end+=1
    else:
        hap -= A[start]
        start+=1
    if(hap == M):
        ans += 1

print(ans)