# 아이디어1. 원형 수열을 기존 배열을 두 배로 늘려 처리하기
# 아이디어2. 슬라이딩 윈도우 사용
# 아이디어3. 누적합

def solution(elements):
    n = len(elements)
    extended_elements = elements + elements
    unique_sums = set()
    
    for length in range(1, n + 1):  # 부분 수열 길이
        current_sum = sum(elements[:length])  # 초기 부분 수열 합
        unique_sums.add(current_sum)
        for start in range(1, n):  # 슬라이딩 윈도우
            current_sum = current_sum - extended_elements[start - 1] + extended_elements[start + length - 1]
            unique_sums.add(current_sum)
    
    return len(unique_sums)
