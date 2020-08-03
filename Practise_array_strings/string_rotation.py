'''
Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

if there is a way to spilt s1 into x and y such that xy = s1 and yx = s2
here yx will always be a substring of xyxy
i.e s2 will always be a substring of s1s1
'''

def isRotation(s1,s2):
    len1 = len(s1)
    if(len1 == len(s2) and len1 > 0):
        s1s1 = s1 + s1
        if(s2 in s1s1):
            return True
    return False

print(isRotation("waterbottle","erbottlewat"))