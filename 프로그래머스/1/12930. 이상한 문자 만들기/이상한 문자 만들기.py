def solution(s):
    strarr = s.split(" ")
    answer = ''
    iter = 0
    for i in strarr:
        n = 0
        word = ''
        for j in i:
            if (n % 2) == 0:
                word += j.upper()
            else:
                word += j.lower()
            n = n + 1
        answer += word
        if(iter != len(strarr)-1):
            answer += ' '
        iter += 1
    return answer