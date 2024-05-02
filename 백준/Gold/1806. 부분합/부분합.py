N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
ans = 0
hap = 0

while(True):
    if(hap < S):
        if(end == N):
            break
        hap += arr[end]
        end+=1
    else:
        hap -= arr[start]
        start+=1
        if(ans == 0 or ans > end-start+1):
            ans = (end-start+1)

print(ans)