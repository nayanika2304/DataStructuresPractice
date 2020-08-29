'''
A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width. Implement a function that draws a horizontal line from (xl, y) to (x2 J y) .
The method signature should look something like:
drawLine(byte[] screen, int width, int xl, int x2, int y)
'''

def draw_line(screen, width, x1, x2, y):
    index_start = y*width + x1
    line_width = x2 - x1 + 1
    for i in range(line_width):
        screen[index_start + i] = 255