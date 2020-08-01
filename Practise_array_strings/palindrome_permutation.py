'''
Given a string, write a function to check if it is a permutation of a palindrome.


To be more precise, strings with even length (after removing all non-letter characters) must have all even counts of characters.
Strings of an odd length must have exactly one character with an odd count.
Of course, an "even" string can't have an odd number of exactly one character, otherwise it wouldn't be an even-length string (an odd number + many even numbers =an odd number).
Likewise, a string with odd length can't have all characters with even counts (sum of evens is even).


It's therefore sufficient to say that, to be a permutation of a palindrome,
a string can have no more than one character that is odd.
This will cover both the odd and the even cases.'
This means the string is either of even length or an odd length with just exactly one character with an odd count.


So, we can check to see that a number has exactly one 1 because if we subtract 1 from it
and then AND it with the new number, we should get 0.
'''

def is_palin_perm(input_str):
    input_str = input_str.replace(' ','')
    input_str = input_str.lower()

    d = dict()
    for i in input_str:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v% 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palin_perm('This is not a palindrome permutation'))
