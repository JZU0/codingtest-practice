# 이분 탐색
def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    min_val = end
    while start <= end:
        level = (start + end) // 2
        temp = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                temp += times[i]
            else:
                # 이전 시간이 없는 경우
                gap = diffs[i] - level
                if i == 0:
                    temp += (gap+1) * times[i] 
                else:
                    temp += (gap) * (times[i]+times[i-1]) + times[i]
            if limit < temp:
                break
        if limit >= temp:
            min_val = min(min_val,level)
            end = level - 1
        else:
            start = level + 1
    return min_val