from collections import Counter

def solution(want, number, discount):
    arr = Counter({want[i]: number[i] for i in range(len(want))})
    temp = Counter(discount[:10]) 
    answer = 0
    start = 0
    end = 10

    while end < len(discount):
        if arr == temp:
            answer += 1

        temp[discount[start]] -= 1
        if temp[discount[start]] == 0:
            del temp[discount[start]]

        temp[discount[end]] += 1

        start += 1
        end += 1

    if arr == temp:
        answer += 1

    return answer
