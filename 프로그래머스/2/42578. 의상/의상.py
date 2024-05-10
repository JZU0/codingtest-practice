def solution(clothes):
    answer = 1
    cloth_dict = {}
    
    for c in clothes:
        if not c[1] in cloth_dict:
            cloth_dict[c[1]] = 1
        else: 
            cloth_dict[c[1]] += 1
            
    for d in cloth_dict:
        answer *= (cloth_dict[d] + 1)           
    return answer-1