# (Stack with Node top + length counter)
# (Stack with Node top + length counter)
# ------------------------------------------------
# This approach is simpler: Stack itself manages the top pointer and length.
# Advantage: We can check stack size in O(1) using the 'length' attribute.

# Node class (same as before)
class Node:
    def __init__(self, value):
        self.value = value      # data stored in this node
        self.next = None        # reference to next node

# Stack class directly manages nodes
class Stack:
    def __init__(self):
        self.top = None         # points to top node of stack
        self.length = 0         # keeps count of number of nodes (O(1) size check)

    def push(self, value):
        # Create new node and insert at top
        new_node = Node(value)
        new_node.next = self.top  # link new node with current top
        self.top = new_node       # update top pointer
        self.length += 1          # increase size counter

    def pop(self):
        # Remove and return top element
        if self.top is None:
            return "Stack is empty"
        popped_node = self.top        # store current top
        self.top = self.top.next      # move top pointer to next node
        self.length -= 1              # decrease size counter
        return popped_node.value      # return popped value

    def peek(self):
        # Return top value if exists
        return self.top.value if self.top else "Stack is empty"

    def is_empty(self):
        # Check if stack is empty
        return self.top is None

    def clear(self):
        # Clear stack completely
        self.top = None
        self.length = 0

    def __len__(self):
        # Built-in len() support
        return self.length

    def __str__(self):
        # Return stack elements from top to bottom as a string
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)  # e.g., "3 -> 2 -> 1"

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)  # Push 1 -> top=1
    stack.push(2)  # Push 2 -> top=2
    stack.push(3)  # Push 3 -> top=3
    print("Stack:", stack)        # Output: 3 -> 2 -> 1
    print("Popped:", stack.pop()) # Removes 3
    print("Peek:", stack.peek())  # Should show 2
    print("Length:", len(stack))  # Should be 2

