import sys
input = sys.stdin.readline

N = int(input())

money = list(map(int, input().split()))

limit = int(input())

start = 0
end = limit

if(sum(money) <= limit):
        print(max(money))
else: 
    while start <= end:
        mid = (start+end) // 2
        total = 0
        for m in money:
            if(m > mid):
                total += mid
            else:
                total += m
        if (total > limit) :
            end = mid - 1
        else :
            start = mid + 1
            result = mid
    print(result)