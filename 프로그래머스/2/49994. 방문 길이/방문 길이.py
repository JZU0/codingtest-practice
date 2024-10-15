def solution(dirs):
    visited = set()
    arr = list(dirs)
    ix, iy = (0,0)
    for a in arr:
        if(a == 'U'):
            dx, dy = (0,1)
        elif(a == 'D'):
            dx, dy = (0,-1)
        elif(a == 'L'):
            dx, dy = (-1,0)
        elif(a == 'R'):
            dx, dy = (1,0)
        if(-5 <= ix + dx <= 5 and -5 <= iy + dy <= 5):
            cx, cy = ix + dx, iy + dy
            visited.add((ix, iy, cx, cy)) 
            visited.add((cx, cy, ix, iy))
            ix, iy = cx, cy    
    return len(visited) // 2