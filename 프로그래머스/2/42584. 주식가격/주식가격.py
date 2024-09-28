def solution(prices):
    stack = []
    answer = [len(prices)-1] * len(prices)

    for i, price in enumerate(prices):
        if(i==len(prices)-1):
            while stack:
                idx = stack.pop()
                answer[idx] = i-idx
            answer[i]=0
            return answer
        while stack and prices[stack[-1]] > price:
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)
    return answer