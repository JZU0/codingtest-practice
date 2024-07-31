def isprimenumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def backtracking(arr, num_arr, m, tmp, results):
    if len(tmp) == m:
        num = int("".join(map(str, tmp)))
        results.add(num)
        return

    for i in range(len(num_arr)):
        tmp.append(num_arr[i])
        backtracking(arr, num_arr[:i] + num_arr[i+1:], m, tmp, results)
        tmp.pop()

def solution(numbers):
    arr = list(numbers)
    num_arr = arr[:]
    results = set()

    for m in range(1, len(arr) + 1):
        backtracking(arr, num_arr, m, [], results)

    answer = 0
    for num in results:
        if isprimenumber(num):
            answer += 1

    return answer