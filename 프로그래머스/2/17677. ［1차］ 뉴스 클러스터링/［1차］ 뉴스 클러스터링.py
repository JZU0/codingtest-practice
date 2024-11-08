from collections import Counter

def func(s):
    s = s.lower()
    temp = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            temp.append(s[i] + s[i+1])
    return temp

def solution(str1, str2):
    temp1 = Counter(func(str1))
    temp2 = Counter(func(str2))
    
    intersection_size = sum((temp1 & temp2).values())
    union_size = sum((temp1 | temp2).values())
    
    if union_size == 0:
        answer = 1
    else:
        answer = intersection_size / union_size
    
    return int(answer * 65536)