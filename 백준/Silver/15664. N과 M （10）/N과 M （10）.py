import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_arr = (list(map(int, input().split())))
num_arr.sort()

dictionary = {i + 1: num_arr[i] for i in range(len(num_arr))}

arr = []
key_arr = []
answer = []

def backtracking():
    if(len(arr) == M):
        ans = " ".join(map(str, arr))
        if ans not in answer:
            answer.append(ans)
            print(ans)
        return
    
    for k in dictionary.keys():
        if not arr or (k not in key_arr and arr[-1] <= dictionary[k]) :
            key_arr.append(k)
            arr.append(dictionary[k])
            backtracking()
            arr.pop()
            key_arr.pop()

backtracking()