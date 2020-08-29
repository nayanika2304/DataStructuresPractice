'''
You are given two 32-bit numbers, Nand M, and two bit positions, i and
j. Write a method to insert Minto N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
'''
def insert_N_into_M(N, M, i, j):
    N_num = int(N, 2)
    M_num = int(M, 2)
    print(1 << i)
    n_mask = (~0 << (j + 1)) | ((1 << i) - 1)
    n_cleared = N_num & n_mask
    m_shifted = M_num << i
    result = n_cleared | m_shifted

    return int_to_binary_string(result)


def int_to_binary_string(num):
    return bin(num)[2:]

