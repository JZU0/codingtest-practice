def solution(nums):
    len_arr = len(nums)
    pick = len(nums) // 2
    
    type = {}
    
    for n in nums:
        if not n in type:
            type[n] = 1
    
    answer = len(type)
    
    if(answer >= pick):
        return pick
    else:
        return answer