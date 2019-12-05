'''
Given 2 strings,check whether it is isomorphic.If it is not isomorphic print '-1'.
Input Size : |s| <= 100000(complexity O(nlogn))
Sample Testcase :
INPUT
aab xxy
OUTPUT
yes
'''
def isIso(a, b):
    m = {} # mapping of each character in a to b
    r = {} # mapping of each character in b to a
    for i, c in enumerate(a):
        if c in m:
            if b[i] != m[c]:
                return 'no'
        else:
            m[c] = b[i]
        if b[i] in r:
            if c != r[b[i]]:
                return 'no'
        else:
            r[b[i]] = c
    return 'yes'
m=list(input().split(' '))
l=m[0]
r=m[1]
print(isIso(l,r)) 
