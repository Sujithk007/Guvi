'''
Given a number N and an array of N integers, find the sum of all the negative numbers in the array.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
3 0
OUTPUT
0
'''
m=int(input())
n=list(map(int,input().split()))
s=0
for i in n:
  if(i<0):
    s=s+i
print(s)
