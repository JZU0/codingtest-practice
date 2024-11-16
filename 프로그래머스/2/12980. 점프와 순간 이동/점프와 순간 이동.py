# def solution(n):
#     ans = 0
#     dp = [float('inf')] * (n + 1)
#     dp[1] = 1
#     for i in range(1,n):
#         if(i*2 <= n):
#             dp[i*2] = dp[i]
#         dp[i+1] = min(dp[i+1], dp[i]+1)
#     return dp[n]
# 시간 복잡도 n

def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:  
            n //= 2     
        else:           
            n -= 1      
            ans += 1    
    return ans