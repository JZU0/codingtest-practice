import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        min_val = heapq.heappop(scoville)
        if(min_val >= K):
            break
        else:
            if(len(scoville) < 1):
                return -1
            new_val = min_val + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, new_val)
            answer += 1
    return answer