N, type = input().split()
N = int(N)

arr = [input() for _ in range(N)]

temp = set(arr)

length = len(temp)

if type == 'Y':
    print(length)
elif type == 'F':
    print(length // 2)
else:
    print(length // 3)