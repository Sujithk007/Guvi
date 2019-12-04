'''
Write a program to print the sum of the first K natural numbers.
Input Size : n <= 100000
Sample Testcase :
INPUT
3
OUTPUT
6
'''
m=int(input())
l=[i for i in range(1,m+1)]
print(sum(l))
