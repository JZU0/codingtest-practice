def solution(distance, rocks, n):
    start, end = 0, distance
    answer = 0
    rocks.sort()
    rocks.append(distance)
    while start <= end:
        removerock = 0
        mid = (start + end) // 2
        prev = 0
        for r in rocks:
            gap = r - prev
            if(gap < mid):
                removerock += 1
                if(removerock > n):
                    break
            else:
                prev = r

        if(removerock > n):
            end = mid-1
        else:
            start = mid + 1
            answer = mid
    return answer