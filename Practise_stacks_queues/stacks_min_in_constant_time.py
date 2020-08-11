from collections import deque


class MinStack:
    # constructor
    def __init__(self):

        # main stack to store elements
        self.s = deque()

        # auxiliary stack to store min elements
        self.aux = deque()

    # Inserts a given element on top of the stack
    def push(self, x):

        # push the given element into main stack
        self.s.append(x)

        # if auxiliary stack is empty, push the given element into it
        if not self.aux:
            self.aux.append(x)

        else:
            # push the given element into the auxiliary stack
            # if it is less than or equal to the current minimum
            if self.aux[-1] >= x:
                self.aux.append(x)

    # Removes top element from the stack and returns it
    def pop(self):

        if self.empty():
            print("Stack underflow")
            return -1

        # remove top element from the main stack
        top = self.s.pop()

        # remove top element from the auxiliary stack
        # only if it is minimum
        if top == self.aux[-1]:
            self.aux.pop()

        # return the removed element
        return top

    # Returns top element of the stack
    def peek(self):

        return self.s[-1]

    # Returns number of elements in the stack
    def len(self):

        return self.len(s)

    # Returns true if stack is empty false otherwise
    def empty(self):

        return not self.s

    # Returns the minimum element from the stack in constant time
    def min(self):

        if not self.aux:
            print("Stack underflow")
            return -1
        return self.aux[-1]


if __name__ == '__main__':

    s = MinStack()

    s.push(6)
    print(s.min())  # prints 6

    s.push(7)
    print(s.min())  # prints 6

    s.push(8)
    print(s.min())  # prints 6

    s.push(5)
    print(s.min())  # prints 5

    s.push(3)
    print(s.min())  # prints 3

    s.pop()
    print(s.min())  # prints 5

    s.push(10)
    print(s.min())  # prints 5

    s.pop()
    print(s.min())  # prints 5

    s.pop()
    print(s.min())  # prints 6
