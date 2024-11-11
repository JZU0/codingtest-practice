import math
def solution(n):
    answer = 1
    # 최대로 나올 수 있는 2칸 뛰는 개수
    temp = n // 2
    for i in range(1, temp+1):
        answer += math.factorial(n-i)//(math.factorial(i) * math.factorial(n-i-i))           
    return answer % 1234567