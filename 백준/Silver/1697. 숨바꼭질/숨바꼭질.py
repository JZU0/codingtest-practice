import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
result = [0 for _ in range(100001)]

def bfs(start, end):
    position = deque([start])
    while position:
        curr = position.popleft()
        if(curr == end):
            print(result[curr])
            break
        for i in ["minus", "plus", "double"]:
            if(i == "minus"):
                num = curr - 1
            elif(i=="plus"):
                num = curr + 1
            else:
                num = curr * 2
            if 0 <= num <= 100000 and not result[num]:    
                result[num] = result[curr] + 1
                position.append(num)
        
bfs(N, K)