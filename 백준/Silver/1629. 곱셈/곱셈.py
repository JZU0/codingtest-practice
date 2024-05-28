import sys

A, B, C = map(int, sys.stdin.readline().split())

def mod_exp(a, b, c):
    if c == 1:
        return 0
    if b == 0:
        return 1
    if b % 2 == 0:
        half = mod_exp(a, b // 2, c)
        return (half * half) % c
    else:
        return (a * mod_exp(a, b - 1, c)) % c

print(mod_exp(A, B, C))