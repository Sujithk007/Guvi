# Given a string as input, you have to reverse the string by 
# keeping the punctuation and spaces intact.
#  You have to modify the source
# string itself without creating another string.

# Input Description:
# 1 <= string length <= 500

# Output Description:
# Print the string in reverse

# Sample Input:
# A man, in the boat says: I see 1-2-3 in the sky
# Sample Output:
# y kse, ht ni3 21ee sIsy: a sta o-b-e ht nin amA

m = list(input())
i = 0
j = len(m)-1
while(i <= j):
    if(m[i] in [' ', ',', '?', ':', '/', '-']):
        i = i+1
    elif(m[j] in [' ', ',', '?', ':', '/', '-']):
        j = j-1
    else:
        m[i], m[j] = m[j], m[i]
        i = i+1
        j = j-1
print(''.join(m))
