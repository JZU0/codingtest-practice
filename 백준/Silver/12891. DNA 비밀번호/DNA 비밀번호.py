import sys

S, P= map(int, sys.stdin.readline().split())
data = list(sys.stdin.readline().strip())

DNA = list(map(int, sys.stdin.readline().split()))

dict= {}
dict['A'] = DNA[0]
dict['C'] = DNA[1]
dict['G'] = DNA[2]
dict['T'] = DNA[3]

pwd_cnt = 0

a_cnt = 0
c_cnt = 0
g_cnt = 0
t_cnt = 0

def check(str):
    global a_cnt, c_cnt, g_cnt, t_cnt
    if str == 'A':
        a_cnt += 1
    elif str == 'C':
        c_cnt += 1
    elif str == 'G':
        g_cnt += 1
    elif str == 'T':
        t_cnt += 1

def minuscheck(str):
    global a_cnt, c_cnt, g_cnt, t_cnt
    if str == 'A':
        a_cnt -= 1
    elif str == 'C':
        c_cnt -= 1
    elif str == 'G':
        g_cnt -= 1
    elif str == 'T':
        t_cnt -= 1

def anscheck():
    global pwd_cnt
    if(a_cnt >= dict['A'] and
       c_cnt >= dict['C'] and
       g_cnt >= dict['G'] and
       t_cnt >= dict['T']):
        pwd_cnt += 1

for k in range(0,P):
    check(data[k])

anscheck()

for i in range(P, S):
    minuscheck(data[i-P])
    check(data[i])
    anscheck()

print(pwd_cnt)
