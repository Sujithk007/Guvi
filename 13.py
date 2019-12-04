'''
Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
Sample Testcase :
INPUT
5 5
OUTPUT
yes
'''
import math
m,n= map(int,input().split(' '))
x=m*n
root = math.sqrt(x)
if int(root + 0.5) ** 2 == x:
    print("yes")
else:
    print("no")
