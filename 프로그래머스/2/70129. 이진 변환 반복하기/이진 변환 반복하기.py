def solution(s):
    answer = []
    cnt = 0
    count_of_zeroes = 0
    binary_representation = ''
    while s != '1':
        new = s.replace('0','')
        count_of_zeroes += s.count('0')
        str_len = len(new)
        binary_representation = bin(str_len)[2:]
        s = binary_representation
        cnt += 1
    answer.append(cnt)
    answer.append(count_of_zeroes)
        
    return answer