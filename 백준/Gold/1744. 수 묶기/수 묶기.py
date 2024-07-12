import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input().strip()) for _ in range(N)]

cnt = 0
flag = 0
for a in arr:
    if(a > 1):
        cnt += 1

if(cnt % 2 ==0):
    flag = 1

if(N==1):
    print(arr[0])
    exit()

arr.sort()

total = 0
i = 1

while True:
    if(i > N-1):
        break
    prev = arr[i-1]
    if(arr[i] <= 0):
        total += prev * arr[i]
        if(i == N-2):
            total += arr[N-1]
            break
        i += 2
    elif(prev > 1):
        if(flag == 0):
            flag = 1
            total += prev
            i += 1
            continue
        total += prev * arr[i]
        if(i == N-2):
            total += arr[N-1]
            break
        i += 2
    else :
        if(i == N-1):
            total += prev + arr[i]
        else:      
            total += prev 
        i += 1

print(total)