def solution(topping):
    temp = {}
    left_temp = set()
    answer = 0
    
    for t in topping:
        if t in temp:
            temp[t] += 1
        else:
            temp[t] = 1
            
    for t in topping:
        left_temp.add(t)
        temp[t] -= 1
        if(temp[t] == 0):
            del temp[t]
        if(len(left_temp)==len(temp)):
            answer += 1

    return answer