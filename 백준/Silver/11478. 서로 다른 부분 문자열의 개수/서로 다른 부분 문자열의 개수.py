# 시간 줄여보기
# 딕셔너리 -> set으로 변경

import sys

S = sys.stdin.readline().strip()

# str_hash = {}
# ans = 0

# for i in range(1, len(S)):
#     for j in range(0, len(S)-i+1):
#         s = S[j:j+i]
#         if not s in str_hash:
#          str_hash[s] = 1
#          ans += 1

# print(ans+1)

ans = set()

for i in range(1, len(S)):
    for j in range(0, len(S)-i+1):
        sub_string = S[j:j+i]
        if not sub_string in ans:
            ans.add(sub_string)

print(len(ans) + 1)