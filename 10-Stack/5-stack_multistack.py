#(Multiple stacks in one array)
# (Multiple stacks in one array)
# ------------------------------------------------
# This approach stores multiple stacks (fixed number) inside a single array.
# Useful when memory is limited, and we want multiple stacks without
# creating separate linked lists or arrays for each stack.

class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3  # Total number of stacks (here we are using 3)
        # Single array divided into equal parts for each stack
        self.array = [0] * (stacksize * self.numstacks)
        # Array to keep track of how many elements each stack currently has
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize  # Max capacity of each stack

    def isFull(self, stacknum):
        # True if this particular stack is at its max capacity
        return self.sizes[stacknum] == self.stacksize

    def isEmpty(self, stacknum):
        # True if this stack has no elements
        return self.sizes[stacknum] == 0

    def indexOfTop(self, stacknum):
        # Find index of the "top" element in the big array for a given stack
        offset = stacknum * self.stacksize  # starting index of this stack
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        # Insert element into the given stack
        if self.isFull(stacknum):
            raise Exception("Stack is full")
        self.sizes[stacknum] += 1  # Increase size of this stack
        self.array[self.indexOfTop(stacknum)] = item  # Place item at top index

    def pop(self, stacknum):
        # Remove top element from a given stack
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        value = self.array[self.indexOfTop(stacknum)]  # Get top value
        self.array[self.indexOfTop(stacknum)] = 0      # Clear it from array
        self.sizes[stacknum] -= 1                     # Decrease stack size
        return value

    def peek(self, stacknum):
        # Get top element without removing
        if self.isEmpty(stacknum):
            raise Exception("Stack is empty")
        return self.array[self.indexOfTop(stacknum)]

# Example usage
if __name__ == "__main__":
    stack = MultiStack(2)   # Creates 3 stacks, each can hold max 2 elements

    # Push elements into different stacks
    stack.push(10, 0)       # Push 10 into Stack 0
    stack.push(20, 1)       # Push 20 into Stack 1
    stack.push(30, 2)       # Push 30 into Stack 2

    # Peek top of Stack 0
    print("Top of Stack 0:", stack.peek(0))  # Output: 10

    # Pop from Stack 1
    print("Popped from Stack 1:", stack.pop(1))  # Output: 20
