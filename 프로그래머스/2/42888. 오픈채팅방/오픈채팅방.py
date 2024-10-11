def solution(record):
    data = {}
    temp = []
    answer = []
    for r in record:
        value = r.split(" ")
        temp.append([value[0],value[1]])
        if value[0] != 'Leave':
            data[value[1]]=value[2]
    for t in temp:
        if(t[0]=='Enter'):
            answer.append(data[t[1]]+'님이 들어왔습니다.')
        if(t[0]=='Leave'):
            answer.append(data[t[1]]+'님이 나갔습니다.')
    return answer