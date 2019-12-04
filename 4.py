'''
Given a number N, find its next immediate greater power of 2.
Input Size : N <= 1000
Sample Testcase :
INPUT
4
OUTPUT
8
'''
m=int(input())
t=0
j=1
while(m>=t):
    t=2**j
    j=j+1
print(t)
