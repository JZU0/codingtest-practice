def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def solution(balls, share):
    answer = factorial_iterative(balls) / (factorial_iterative(balls-share) * factorial_iterative(share))
    return answer