import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())

sushi = [int(input().strip()) for _ in range(N)]

check = [0]*(d+1)
check[c] = 1
total = 1
result = []

for i in range(k):
    if not check[sushi[i%N]]:
        total += 1
    check[sushi[i%N]] += 1

for i in range(N):
    start = sushi[i%N]
    end = sushi[(i+k)%N]

    check[start] -= 1
    if not check[start]:
        total -= 1

    if not check[end]:
        total += 1

    check[end] += 1
    result.append(total)

print(max(result))