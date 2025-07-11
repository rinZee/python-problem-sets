#Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

def first_unique(s):
    dict = {}
    for letter in s:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    
    
    return s.find("e")
    #for i in range(len(s)):
     #   if dict[s[i]] == 1:
     #       return i
    #return -1
        
s = "leetcode"
s2 = "loveleetcode"

s3 = "aabb"

unique = first_unique(s), first_unique(s2), first_unique(s3)
print(unique)

#Examples:
#Output: 0