
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
