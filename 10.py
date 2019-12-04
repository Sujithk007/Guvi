'''
Given a number N, print 'yes' if it is composite else print 'no'.
Sample Testcase :
INPUT
123
OUTPUT
yes
'''
m=int(input())
cnt=0
for i in range(2,m):
    if(m%i==0):
        cnt=cnt+1
        break
if(cnt==0):
    print('no')
else:
    print('yes')
