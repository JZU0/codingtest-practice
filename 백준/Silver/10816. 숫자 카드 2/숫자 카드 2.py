import sys
input = sys.stdin.readline

N = int(input())

sang = list(map(int, input().split()))

M = int(input())

card = list(map(int, input().split()))

dict = {}

for s in sang:
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

for c in card:
  if c in dict:
    print(dict[c], end=' ')
  else:
     print(0, end=' ')     