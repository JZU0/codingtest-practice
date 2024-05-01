N, M = map(int, input().split())
height = list(map(int, input().split()))

h_min = 0
h_max = max(height)*2

tree = 0
treearr = []

while(h_min <= h_max):
    mid = (h_min + h_max) // 2
    tree = 0
    for i in height:
        if(i>=mid):
            tree += i-mid
    if (tree < M):
        h_max = mid - 1
    elif (tree >= M):
        treearr.append(mid)
        h_min = mid + 1

if not treearr:
    print(-1)
else:
    print(max(treearr))