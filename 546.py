'''
You are given a large number made of only 0’s and 1’s.Your task is to find the max no of consecutive 1’s. If there are no 1’s print -1

Input Description:
A large number ‘n’

Output Description:
Print the max no of consecutive 1 in the number

Sample Input :
101011111

Sample Output :
5
""

r=list(input())
max1,m=0,0
for i in range(len(r)):
    if(r[i]=='1'):
        m=m+1
        if(m>max1):
            max1=m
    else:
        m=0
if(max1==0):
    print('-1')
else:
    print(max1)
