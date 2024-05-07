N = int(input())
time = []
for i in range(0, N):
    s, e = map(int, input().split())
    time.append([s, e])

time.sort(key=lambda x: [x[1], x[0]])

meeting = time[0]
ans = 1

for t in range(1, N):
    if(time[t][0] >= meeting[1]):
        meeting = time[t]
        ans += 1

print(ans)  