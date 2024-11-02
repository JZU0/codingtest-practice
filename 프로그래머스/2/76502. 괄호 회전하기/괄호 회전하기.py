def is_valid_bracket_string(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in "({[": 
            stack.append(char)
        elif char in ")}]":  
            if stack and stack[-1] == bracket_pairs[char]:  
                stack.pop()  
            else:
                return False  
    return not stack  

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]  
        if is_valid_bracket_string(rotated_s):  
            count += 1
    return count
