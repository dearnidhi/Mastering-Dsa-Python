# (Stack with max size)
# isEmpty

class stack:
    def __init__(self , maxsize):
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
            return "Stack is Full"
        self.list.append(values)
        return "Inserted"
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.list[-1]
    
    def delete(self):
        self.list = []


customstack = stack(4)

print(customstack.isEmpty)
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
print(customstack.delete())


    
    


   