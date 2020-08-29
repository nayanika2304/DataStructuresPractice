'''
You have an integer and you can flip exactly one bit from a 13 to a 1.
Write code to find the length of the longest sequence of ls you could create.

using sliding window approach
'''


def find_longest_sequence(num):
    previous = 0
    current_run = 0
    current_max = 1

    while num:
        print(bin(num))
        current_bit = num & 1
        num = num >> 1

        if current_bit == 1:
            current_run += 1
        else:
            previous = current_run
            current_run = 0

        current_max = max(current_max, previous + current_run + 1)

    return current_max

print(find_longest_sequence(1775))