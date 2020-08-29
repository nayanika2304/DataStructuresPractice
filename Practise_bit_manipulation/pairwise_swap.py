'''
Write a program to swap odd and even bits in an integer with as few instructions as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''
def pairwise_swap(num):
    even_mask = create_even_mask(num)
    odd_mask = create_odd_mask(num)
    even_cleared = num & even_mask
    odd_cleared = num & odd_mask
    combined = (odd_cleared >> 1) | (even_cleared << 1)
    return (odd_cleared >> 1) | (even_cleared << 1)


def create_odd_mask(num):
    bin_representation = bin(num)[2:]
    bit_length = len(bin_representation)
    bit_sign = '0'
    mask = []

    for i in range(bit_length):
        mask.insert(0, bit_sign)
        bit_sign = '1' if bit_sign == '0' else '0'

    return int(''.join(mask), 2)


def create_even_mask(num):
    bin_representation = bin(num)[2:]
    bit_length = len(bin_representation)
    bit_sign = '1'
    mask = []

    for i in range(bit_length):
        mask.insert(0, bit_sign)
        bit_sign = '1' if bit_sign == '0' else '0'

    return int(''.join(mask), 2)