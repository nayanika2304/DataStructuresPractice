'''
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Best Practise :

Ask if string is ASCII or Unicode. Unicode requires more storage
ASCII has 128-character alphabets
http://sticksandstones.kstrom.com/appen.html

Algo if we can use additional DS - Time complexity O(n) space complexity O(C)

if string length exceeds the unique characters
return false

else
declare an array for T or F for characters
iterate through the array of strings
if bool array has string return false
else
boolarray[chartAt(i)] = true

If we are allowed to modify the input string,
we could sort the string in O( n log( n» time and then linearly check the string for neighboring characters that are identical.
Careful, though: many sorting algorithms take up extra space.
'''
def areCharactersUnique(s):
    # An integer to store presence/absence
    # of 26 characters using its 32 bits
    checker = 0

    for i in range(len(s)):

        val = ord(s[i]) - ord('a')
        # If bit corresponding to current
        # character is already set
        if (checker & (1 << val)) > 0:
            return False

        # set bit in checker
        checker |= (1 << val)

    return True


# Driver code
s = "aaabbccdaa"
if areCharactersUnique(s):
    print("Yes")
else:
    print("No")



