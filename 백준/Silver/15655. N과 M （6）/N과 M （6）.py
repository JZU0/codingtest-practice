import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_arr = (list(map(int, input().split())))
num_arr.sort()

arr = []

def backtracking():
    if(len(arr) == M):
        print(" ".join(map(str, arr)))
        return
    
    for i in num_arr:
        if not arr or (arr[-1] <= i and i not in arr):
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()