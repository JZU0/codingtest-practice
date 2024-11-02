def solution(n, words):
    answer = [0,0]
    prev=''
    temp = set()
    for i, w in enumerate(words):
        if i == 0 :
            prev = w[-1]
        else:
            if prev != w[0] or w in temp:
                return [i%n+1,(i + 1) // n if (i + 1) % n == 0 else (i + 1) // n + 1]
        prev = w[-1]
        temp.add(w)
    return answer