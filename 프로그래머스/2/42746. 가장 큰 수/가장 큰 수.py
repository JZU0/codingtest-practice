def solution(numbers):
    temp = list(map(str, numbers))

    temp.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(temp)
    
    return answer if answer[0] != '0' else '0'