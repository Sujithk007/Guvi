'''
Given a number N, find the nearest greater multiple of 10.
Input Size : N <= 10000
Sample Testcase :
INPUT
3
OUTPUT
10
'''
m=round(int(input()))
if(m%10<5 and m>9):
    while(m%10!=0):
        m=m-1
elif(m%10>4):
    while(m%10!=0):
        m=m+1
else:
    m=10
print(m)
