N, X = map(int, input().split())
visitarr = list(map(int, input().split()))

start = 0
end = X-1
max_visit = 0
max_count = 0
hap = 0

for i in range(0,X):
    max_visit += visitarr[i]

hap = max_visit
max_count = 1
while(end < N-1):
    hap -= visitarr[start]
    start += 1
    end += 1
    hap += visitarr[end]
    if(max_visit == hap):
        max_count += 1
    if(max_visit < hap):
        max_visit = hap 
        max_count = 1

if (max_visit == 0):
    print("SAD")
else:
    print(max_visit)
    print(max_count)