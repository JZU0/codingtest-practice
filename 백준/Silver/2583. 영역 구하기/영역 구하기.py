from collections import deque

# 여기서 핵심 아이디어는 
# 현재 칸이 빈 공간인 경우에만 BFS를 실행한다는 것!

M, N, K = map(int, input().split())

graph = [[0]*N for _ in range(M)]
paint = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    paint.append(((x1, y1), (x2, y2)))

for p in paint:
    x = p[0][0]
    y = p[0][1]
    limit_x = p[1][0]
    limit_y = p[1][1]
    for i in range(x, limit_x):
        for j in range(y, limit_y):
            graph[M-1-j][i] = 1

def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1  # 방문 표시
    area = 1  # 현재 빈 공간의 넓이
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1  # 방문 표시
                area += 1
    return area

def count_empty_areas(graph):
    empty_areas = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                empty_areas.append(bfs(graph, i, j))
    empty_areas.sort()
    return empty_areas

empty_areas = count_empty_areas(graph)
print(len(empty_areas))
print(*empty_areas)