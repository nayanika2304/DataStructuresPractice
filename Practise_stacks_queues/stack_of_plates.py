'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
'''

class StackOfPlates:
    def __init__(self,capacity):
        self.stacks= []
        if capacity < 1:
            raise NameError("A stack is greater than one")
        else:
            self.capacity = capacity

    def push(self,item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)
        print(self.stacks)

    def pop(self):
        if self.stacks == []:
            raise NameError("Stack is empty cannot be popped")
        else:
            popped_data = self.stacks[-1][-1]

            if len(self.stacks[-1]) == -1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]

        return popped_data

    def popAt(self,index):
        '''
        if we need to roll over the data

        '''
        if self.stacks == []:
            raise NameError("Stack is empty")

        elif index -1 > len(self.stacks):
            raise NameError("index is out of range")
        else:
            popped_data = self.stacks[index][-1]

            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            elif len(self.stacks[-1]) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index-1][-1] = self.stacks[index][0]

                for i in range(index,len(self.stacks)):
                    for j in range (0,len(self.stacks[i])-1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks)-1:
                        self.stacks[i][-1] = self.stacks[i+1][0]
                del self.stacks[-1][-1]

                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
            print(self.stacks)
        return popped_data

        '''
        if we can just leave it at it`s capacity
        if (index < 0) or (index > self.last):
            return False
        to_return = self.stacks[index].pop()
        if self.stacks[index].size() <= 0:
            del self.stacks[index]
            self.last = self.last - 1
        return to_return
        '''

if __name__ == '__main__':

    s = StackOfPlates(4)

    s.push(1)


    s.push(2)

    s.push(3)

    s.push(4)

    s.push(5)

    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)

    #print(s.pop())
    #print(s.popAt(1))
    print(s.popAt(0))




