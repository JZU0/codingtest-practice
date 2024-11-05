from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if(cacheSize == 0):
        return len(cities*5)
    for c in cities:
        c = c.lower()
        
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            if(len(cache) == cacheSize):
                cache.popleft()
            cache.append(c)
            answer += 5
    return answer