import heapq

N_info = []
weight = []

N, K = map(int, input().split())
for _ in range(N):
    M, V = map(int, input().split())
    N_info.append([M, V])

for _ in range(K):
    weight.append(int(input()))

N_info.sort(reverse=True)
weight.sort()

q = []
ans = 0

for m in weight:
    while N_info:
        weight, price = N_info.pop()
        if(m>= weight):
            heapq.heappush(q, -price)
        else:
            N_info.append((weight, price))
            break
    if q:
        ans -= heapq.heappop(q)
        
print(ans)