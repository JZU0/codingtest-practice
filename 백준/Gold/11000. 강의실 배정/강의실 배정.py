import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

meeting = []

# 끝나는 시간
heapq.heappush(meeting, q[0][1])

for i in range(1, n):
    if q[i][0] < meeting[0]: 
        heapq.heappush(meeting, q[i][1]) 
    else:
        heapq.heappop(meeting) 
        heapq.heappush(meeting, q[i][1])

print(len(meeting))