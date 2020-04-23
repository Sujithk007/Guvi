# There is one meeting room in Flipkart. 
# There are n meetings in the form of (S [ i ], F [ i ]) 
# where S [ i ] is start time of meeting i and F [ i ] is finish time 
# of meeting i Given a number N followed by 2 arrays S and F of 
# sizes N and N, What is the maximum number of meetings that can be 
# accommodated in the meeting room assuming the room can only accommodate 
# one meeting at a time.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# 3
# 10 12 30
# 20 25 30
# OUTPUT
# 2


def check(s, f):
    n = len(f)
    i = 0
    cnt = 0
    cnt = cnt+1
    for j in range(n):
        if s[j] >= f[i]:
            cnt = cnt+1
            i = j
    return cnt


m = int(input())
s = list(map(int, input().split(' ')))
f = list(map(int, input().split(' ')))
print(check(s, f))
