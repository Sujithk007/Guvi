'''
Check whether the given 4 points form a square or not.
Example:
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes
'''
import math
p1=list(map(int,input().split(' ')))
p2=list(map(int,input().split(' ')))
p3=list(map(int,input().split(' ')))
p4=list(map(int,input().split(' ')))
x1=math.sqrt((p4[0]-p2[0])*(p4[0]-p2[0])+(p4[1]-p2[1])*(p4[1]-p2[1]))
x2=math.sqrt((p3[0]-p1[0])*(p3[0]-p1[0])+(p3[1]-p1[1])*(p3[1]-p1[1]))
if(x1==x2):
    print('yes')
else:
    print('no')
