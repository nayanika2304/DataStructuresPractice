'''
https://www.youtube.com/watch?v=QMlDCR9xyd8
'''
from collections import deque


class MinStack:
    def __init__(self):

        # main stack to store elements
        self.s = deque()

        # variable to store minimum element
        self.min = None

    # Inserts a given element on top of the stack
    def push(self, x):

        if not self.s:
            self.s.append(x)
            self.min = x

        elif x > self.min:
            self.s.append(x)

        else:
            self.s.append(2 * x - self.min)
            self.min = x

    # Removes top element from the stack and returns it
    def pop(self):

        if not self.s:
            self.print("Stack underflow!!")

        top = self.s[-1]
        if top < self.min:
            self.min = 2 * self.min - top
        self.s.pop()

    # Returns the minimum element from the stack in constant time
    def minimum(self):

        return self.min


if __name__ == '__main__':

    s = MinStack()

    s.push(6)
    print(s.minimum())

    s.push(7)
    print(s.minimum())

    s.push(5)
    print(s.minimum())

    s.push(3)
    print(s.minimum())

    s.pop()
    print(s.minimum())

    s.pop()
    print(s.minimum())
