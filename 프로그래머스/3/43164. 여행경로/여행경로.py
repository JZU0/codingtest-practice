# def solution(tickets):
#     answer = ["ICN"]
#     visited = [False]*len(tickets)
#     def dfs(end):
#         answer.append(end)
#         can = []
#         for i, v in enumerate(tickets):
#             s, e = v
#             if(s == end and visited[i]==False):
#                 can.append([e,i])
#         if can:
#             can.sort()
#             visited[can[0][1]] = True
#             dfs(can[0][0])
            
#     init = []
#     for i, v in enumerate(tickets):
#         s, e = v
#         if(s == "ICN"):
#             init.append([e,i])
#     init.sort()
#     visited[init[0][1]] = True
#     dfs(init[0][0])
                
#     return answer

def solution(tickets):
    answer = ["ICN"]
    visited = [False] * len(tickets)

    def dfs(end):
        if len(answer) == len(tickets) + 1: 
            return True
        
        can = []
        for i, v in enumerate(tickets):
            s, e = v
            if s == end and not visited[i]:
                can.append([e, i])
        
        can.sort() 
        
        for e, i in can:
            visited[i] = True
            answer.append(e)
            if dfs(e):  
                return True
            visited[i] = False
            answer.pop()
        
        return False

    init = []
    for i, v in enumerate(tickets):
        s, e = v
        if s == "ICN":
            init.append([e, i])
    
    init.sort()
    for e, i in init:
        visited[i] = True
        answer.append(e)
        if dfs(e): 
            return answer
        visited[i] = False
        answer.pop()

    return answer
