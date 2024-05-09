import sys

N, M = map(int, sys.stdin.readline().split())

url_hash = {}

for _ in range(N):
    url, pwd = sys.stdin.readline().strip().split()
    url_hash[url] = pwd

queries = [sys.stdin.readline().rstrip() for _ in range(M)]

for q in (queries):
    print(url_hash[q])
