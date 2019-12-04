'''
Given 2 numbers N,M. Find their difference and check whether it is even or odd.
Sample Testcase :
INPUT
5 5
OUTPUT
even
'''
a,b=map(int,input().split())
s=a-b
if(s%2==0):
	print('even')
else:
	print('odd')
