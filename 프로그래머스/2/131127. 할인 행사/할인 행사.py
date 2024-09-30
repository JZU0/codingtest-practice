def solution(want, number, discount):
    arr = {}
    temp = {}
    for i in range(len(want)):
        arr[want[i]] = number[i]
    start = -1
    end = 9
    answer = 0
    
    for i in range(10):
        if discount[i] not in temp:
            temp[discount[i]] = 1
        else:
            temp[discount[i]] += 1
        
    while end < len(discount):
        if(arr==temp):
            answer += 1
        start += 1
        if discount[start] in temp:
            temp[discount[start]] -= 1
            if temp[discount[start]] == 0:
                del temp[discount[start]]
        end += 1
        if end < len(discount):  
            if discount[end] not in temp:
                temp[discount[end]] = 1
            else:
                temp[discount[end]] += 1
    return answer