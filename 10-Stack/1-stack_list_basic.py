# (Simple stack with Python list)
class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        value = [str(x) for x in reversed(self.list)]  
        return '\n'.join(value)

    def isEmpty(self):
        return self.list == []  
    def push(self, value):
        self.list.append(value)
        return "inserted"
    def pop(self):
        if self.isEmpty():
            return "it is Empty"
        return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list[-1]
    def delete(self):
        self.list == []

    def size(self):
        return len(self.list)    
customStack = Stack()  
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)

print("peek",customStack.peek())
print("size",customStack.size())
print("after delete",customStack.delete())






