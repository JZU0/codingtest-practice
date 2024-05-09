import sys
       
N = int(sys.stdin.readline().strip())

for _ in range(N):
    result = 1
    cloth_hash = {}
    M = int(sys.stdin.readline().strip())
    for _ in range(M):
        name, type = sys.stdin.readline().strip().split()
        if not type in cloth_hash:
            cloth_hash[type] = 1
        else:
            cloth_hash[type] += 1

    for i in cloth_hash:
        result *= (cloth_hash[i] + 1)
    
    print(result-1)
