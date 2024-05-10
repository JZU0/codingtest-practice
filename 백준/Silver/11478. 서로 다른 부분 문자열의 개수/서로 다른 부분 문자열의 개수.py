import sys

S = sys.stdin.readline().strip()

str_hash = {}
ans = 0

for i in range(1, len(S)):
    for j in range(0, len(S)-i+1):
        s = S[j:j+i]
        if not s in str_hash:
         str_hash[s] = 1

for k in str_hash:
   ans += str_hash[k]

print(ans+1)