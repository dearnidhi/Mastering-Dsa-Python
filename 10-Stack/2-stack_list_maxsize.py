# (Stack with max size)
# isEmpty
class stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []
    def __str__(self):
        values = [str(x) for x in reversed(self.list)] 
        return '\n'.join(values)  
    
    def isEmpty(self):
        return self.list == []
    def isFull(self):
        return len(self.list) == self.maxsize
    def push(self, values):
        if self.isFull():
            return "Stack is full"
        self.list.append(values)
        return "inserted"
    def pop(self):
        if self.isEmpty():
            return "Stack is isEmpty"
        return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is isEmpty"
        return self.list[-1]
    def delete(self):
        self.list = []
customstack=stack(4)    
print(customstack.isEmpty)
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
print(customstack.peek())
print(customstack.pop())
print(customstack.delete())


    
    


   