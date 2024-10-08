def solution(n):
    start, end = 1, 2
    sum = 1
    result = 0
    while start < end:
        if sum < n:
            sum += end
            end += 1
        else:
            if sum == n:
                result += 1
            sum -= start
            start += 1
    return result