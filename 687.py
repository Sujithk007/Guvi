'''
You are given an array of numbers. Print the least occurring element. If there is more than 1 element print all of them in decreasing order of their value.

Input Description:
You are given a number ‘n’ denoting size of array. Next line contains n space separated numbers.

Output Description:
Print the number as mentioned

Sample Input :
9
1 6 4 56 56 56 6 4 2

Sample Output :
2 1
'''
w=int(input())
m=list(map(int,input().split(' ')))
d={}
p=1
r=[]
for i in m:
    d[i]=m.count(i)
for i,j in d.items():
    if(j==1):
        r.append(i)
print(*sorted(r,reverse=True))
