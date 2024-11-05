import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

max_stars_in_trampoline = 0

for i in range(K):
    for j in range(K):
        min_x = min(stars[i][0], stars[j][0])
        min_y = min(stars[i][1], stars[j][1])
        count = 0

        for sx, sy in stars:
            if min_x <= sx <= min_x + L and min_y <= sy <= min_y + L:
                count += 1

        max_stars_in_trampoline = max(max_stars_in_trampoline, count)

result = K - max_stars_in_trampoline
print(result)
