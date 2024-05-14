def solution(s):
    check = []
    for str in s:
        if ( str == '('):
            check.append(str)
        else:
            if not check:
                return False
            check.pop()
    if not check:
        return True
    else: return False