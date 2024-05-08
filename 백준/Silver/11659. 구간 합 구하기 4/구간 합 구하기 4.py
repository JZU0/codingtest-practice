N, M = map(int, input().split())
arr = list(map(int, input().split()))

index_arr = []
sum_arr = [0]*(N+1)

for _ in range(M):
    i, j = map(int, input().split())
    index_arr.append([i, j])

def sumfunc(arr):
    for i in range(1, N+1):
        sum_arr[i] = sum_arr[i-1] + arr[i-1]

sumfunc(arr)

for idx in index_arr:
    print(sum_arr[idx[1]]-sum_arr[idx[0]-1])