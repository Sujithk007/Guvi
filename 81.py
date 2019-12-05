'''
Given 3 points check whether they lie on the same line.If they lie on the same line print 'yes' Otherwise print 'no'.
Sample Testcase :
INPUT
0 1
0 0
0 2
OUTPUT
yes
'''
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
t=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
if(t==0):
    print('yes')
else:
    print('no')
