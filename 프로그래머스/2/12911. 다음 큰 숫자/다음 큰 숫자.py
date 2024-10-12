def solution(n):
    answer = 0
    n_bin = format(n, 'b')
    answer = n+1
    while True:
        answer_bin = format(answer, 'b')
        if(n_bin.count('1')==answer_bin.count('1')):
            return answer
        answer += 1