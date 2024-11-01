def solution(topping):
    right_count = {}
    for t in topping:
        if t in right_count:
            right_count[t] += 1
        else:
            right_count[t] = 1

    left_types = set()
    answer = 0

    for t in topping:
        left_types.add(t)
        right_count[t] -= 1

        if right_count[t] == 0:
            del right_count[t]

        if len(left_types) == len(right_count):
            answer += 1

    return answer
