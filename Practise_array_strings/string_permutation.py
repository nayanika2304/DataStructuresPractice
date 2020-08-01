'''
Check Permutation: Given two strings,
write a method to decide if one is a permutation of the other.

Ask - if case sensitive or considers white space

base case : if the strings are of different length
it cannot be a permutation

two methods :
A) Sorting : if two strings are sorted and then equal, they are in permutation
             it may be O(n^2) or O(nlogn) based on sorting used
B) Count the strings - implemented here

This method assumes that the set of possible characters in both strings is small. In the following implementation, it is assumed that the characters are stored using 8 bit and there can be 256 possible characters.
1) Create count arrays of size 256 for both strings.
    Initialize all values in count arrays as 0.
2) Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
3) Compare count arrays. If both count arrays are same, then return true.
'''

# Python program to check if two strings are
# Permutations of each other
NO_OF_CHARS = 256


# Function to check whether two strings are
# Permutation of each other
def arePermutation(str1, str2):
    # Create two count arrays and initialize
    # all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    # If both strings are of different length.
    # Removing this condition will make the
    # program fail for strings like
    # "aaca" and "aca"
    print(count1)
    if len(str1) != len(str2):
        return 0

    # Compare count arrays
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1


# Driver program to test the above functions
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if arePermutation(str1, str2):
    print("Yes")
else:
    print("No")