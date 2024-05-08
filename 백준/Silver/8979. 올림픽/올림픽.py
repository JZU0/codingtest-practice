N, K = map(int,input().split())

result = {}
for _ in range(N):
    line = input().split()  
    key = int(line[0])  
    values = list(map(int, line[1:]))  
    result[key] = values  

sorted_result = sorted(result.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True)

rank = 1
prevrank = 1
afterrank = 1
if(sorted_result[0][0] == K):
    print(rank)
else:
    for i in range(1,N):
        prevrank = rank
        afterrank += 1
        rank = afterrank
        if(sorted_result[i][1] == sorted_result[i-1][1]):
                rank = prevrank
                afterrank += 1
        if(sorted_result[i][0] == K):
            print(rank)
