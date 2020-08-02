'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

set here will be unique set of characters from the string
list will be a a list of all characters
'''

def compressed_string(string):
    compressed = ''
    if len(string) != set(string):
        for i in set(string):
            count = 0
            for j in list(string):
                if i == j:
                    count += 1
            compressed += i+str(count)
        return compressed
    else:
        return string

print(compressed_string('aabcccccaaa'))