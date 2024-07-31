def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    one_collect = 0
    two = [2,1,2,3,2,4,2,5]
    two_collect = 0
    three = [3,3,1,1,2,2,4,4,5,5]
    three_collect = 0
    
    for i in range(len(answers)):
        value = answers[i]
        if(value == one[i%5]):
            one_collect += 1
        if(value == two[i%8]):
            two_collect += 1
        if(value == three[i%10]):
            three_collect += 1
            
    arr = [[one_collect,1],[two_collect,2],[three_collect,3]]
    arr.sort(key=lambda x: (-x[0], x[1]))

    answer.append(arr[0][1])
    
    if(arr[0][0]==arr[1][0]):
        answer.append(arr[1][1])
    if(arr[0][0]==arr[2][0]):
        answer.append(arr[2][1])
        
    return answer