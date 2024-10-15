def solution(n):
    triangle = [[0] * i for i in range(1, n+1)]
    
    directions = [(1, 0), (0, 1), (-1, -1)]
    
    x, y = 0, 0
    direction_idx = 0
    current_value = 1
    
    for i in range(1, n * (n + 1) // 2 + 1):
        triangle[x][y] = current_value
        current_value += 1
        
        dx, dy = directions[direction_idx]
        nx, ny = x + dx, y + dy
        
        if not (0 <= nx < n and 0 <= ny < len(triangle[nx]) and triangle[nx][ny] == 0):
            direction_idx = (direction_idx + 1) % 3
            dx, dy = directions[direction_idx]
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny
    
    result = []
    for row in triangle:
        result.extend(row)
    
    return result