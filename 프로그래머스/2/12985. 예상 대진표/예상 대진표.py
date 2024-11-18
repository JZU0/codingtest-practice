def sol(x):
    if(x % 2 == 0):
        return x // 2
    else:
        return x // 2 + 1
    
def solution(n,a,b):
    answer = 1

    while n >= 2:
        if(a%2==0 and b%2==1 and a-b==1):
            return answer
        elif(a%2==1 and b%2==0 and b-a==1):
            return answer
        a = sol(a)
        b = sol(b)
        n = n // 2
        answer += 1
