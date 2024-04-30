def solution(s):
    strlen = len(s) == 4 or len(s) == 6
    num = s.isdigit()
    return strlen and num