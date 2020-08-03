'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees.

in place means swapping so

We perform such a swap on each layer, starting from the outermost layer and working our way inwards.
(Alternatively, we could start from the inner layer and work outwards.)
'''

def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]


            # left -> top

            matrix[layer][i] = matrix[-i - 1][layer]


            # bottom -> left

            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]


            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix



print(rotate_matrix([
[1 ,2 ,3 ,4],
[5 ,6 ,7 ,8],
[9 ,10 ,11 ,12],
[13 ,14 ,15 ,16]
]))