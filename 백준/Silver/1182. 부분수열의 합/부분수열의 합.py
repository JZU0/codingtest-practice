import sys
input = sys.stdin.readline

N, S = map(int, input().split())

num_arr = (list(map(int, input().split())))

arr = []
cnt = 0

def backtracking(start):
    # print(arr)
    # print(sum(arr))
    # print("start" , start)
    global cnt
    if(sum(arr) == S and len(arr) > 0):
        cnt += 1
    
    for i in range(start, N):
            arr.append(num_arr[i])
            backtracking(i+1)
            arr.pop()

backtracking(0)
print(cnt)