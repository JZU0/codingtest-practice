def solution(participant, completion):
    p_hash = {}
    ans = ''
    for p in participant:
        if not p in p_hash:
            p_hash[p] = 1
        else:
            p_hash[p] += 1
    for c in completion:
        if c in p_hash:
            p_hash[c] -= 1
            
    for h in p_hash:
        if(p_hash[h] == 1):
            ans = h
    return ans