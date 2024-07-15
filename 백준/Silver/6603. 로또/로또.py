import sys
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline

def backtracking(ans, remaining_list, result):
    if len(ans) == 6:
        value = " ".join(map(str, ans))
        if value not in result:
            result.append(value)
            print(value)
        return
    for i in range(len(remaining_list)):
        if remaining_list[i] not in ans:
            ans.append(remaining_list[i])
            backtracking(ans, remaining_list[i+1:], result)
            ans.pop()


while True:
    arr = input().split()

    first_value = int(arr[0])
    if(first_value == 0):
        break
    remaining_list = list(map(int, arr[1:]))

    result = []
    backtracking([], remaining_list, result)
    print()