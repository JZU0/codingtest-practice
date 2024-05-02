import math

N = int(input())

oddnumarr = [True for i in range(N+1)]
arr = []
def oddnum(k):
    for i in range(2,int(math.sqrt(k))+1):
        if oddnumarr[i] == True:
            j = 2
            while i * j <= k:
                oddnumarr[i*j] = False
                j += 1
    for i in range(2, N+1):
        if oddnumarr[i]:
            arr.append(i)
oddnum(N)

start = 0
end = 0
ans = 0
hap = 0

while(True):
    if(hap < N):
        if(end == len(arr)):
            break
        hap += arr[end]
        end+=1
    else:
        hap -= arr[start]
        start+=1
    if (hap == N):
        ans += 1

print(ans)