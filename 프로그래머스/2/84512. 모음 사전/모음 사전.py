def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    position_weights = [781, 156, 31, 6, 1]  # 각 자리에 대한 가중치
    answer = 0
    
    for i, char in enumerate(word):
        # 각 자리의 문자가 몇 번째 모음인지 찾음
        idx = vowels.index(char)
        # 그 자리에 해당하는 가중치 곱하기
        answer += idx * position_weights[i] + 1  # 1은 현재 자리의 값을 더하기 위함
    
    return answer