def solution(sizes):
    answer = 0
    max0 = 0
    max1 = 0
    for s in sizes:
        tmp = 0
        if(s[0] > s[1]):
            tmp = s[0]
            s[0] = s[1]
            s[1] = tmp
        if(s[0] > max0):
            max0 = s[0]
        if(s[1] > max1):
            max1 = s[1]
    return max0 * max1