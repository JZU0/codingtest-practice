def solution(k, tangerine):
    answer = 0
    cnt = {}
    arr = []
    for t in tangerine:
        if t in cnt:
            cnt[t] += 1
        else:
            cnt[t] = 1
    
    for key, value in cnt.items():
        arr.append([value,key])
    
    arr.sort(reverse=True)
    while True:
        if(k <= 0):
            return answer
        k -= arr[answer][0]
        answer += 1
    return answer