'''
Given a number N, print the product of the digits.
Input Size : N <= 100000000000
Sample Testcase :
INPUT
2143
OUTPUT
24
'''
n=input()
m=list(n)
s=0
p=1
for i in m:
    p=p*int(i)
print(p)
