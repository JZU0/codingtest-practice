from collections import defaultdict

dict = defaultdict(int)

alpha = input()
alpha = alpha.upper()

for a in alpha:
    dict[a] += 1

max_val = 0
max_key = 'a'
for k, v in dict.items():
    if max_val < v:  
        max_val = v  
        max_key = k

flag = 0
for v in dict.values():
    if(max_val==v):
        flag += 1
    if flag > 1:
        print('?')
        break
if flag == 1:
    print(max_key)