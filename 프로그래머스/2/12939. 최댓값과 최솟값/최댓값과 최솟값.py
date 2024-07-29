def solution(s):
    arr = s.split()
    arr_int = list(map(int, arr))
    answer = str(min(arr_int)) + " " + str(max(arr_int))
    return answer