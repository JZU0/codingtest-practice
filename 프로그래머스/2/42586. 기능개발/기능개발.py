def solution(progresses, speeds):
    answer = []
    time = []
    for i in range(len(progresses)):
        n = (100 - progresses[i]) // speeds[i] 
        if((100 - progresses[i]) % speeds[i]) > 0:
            n += 1
        time.append(n)
    # 	[5, 10, 1, 1, 20, 1]
    #   [7, 3, 9]
        
    cnt = 1
    large = time[0]
    for j in range(1,len(time)):
        if(large >= time[j]):
            cnt += 1
        else:
            large = time[j]
            answer.append(cnt)
            cnt = 1
        if (j == len(time)-1 and large >= time[j]):
            answer.append(++cnt)
            
    return answer