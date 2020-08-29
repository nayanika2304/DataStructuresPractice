'''
Write a function to determine the number of bits you would need to flip to
convert integer A to integer B.
'''

def test_flip_to_make_equal(n1, n2):
    different_bits = n1 ^ n2
    count = 0
    while different_bits:
        different_bits = different_bits & (different_bits - 1)
        count += 1
    return count