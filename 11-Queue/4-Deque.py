#C:\Users\window 11\Desktop\dsa\DSA-2025\Queue\Deque.py
# How to use collections.deque as a FIFO queue:

# Importing deque from Python's collections module
# deque stands for "double-ended queue" - it allows fast appends and pops from both ends.
from collections import deque

# Creating a deque object with a maximum length of 3
# maxlen=3 means deque will hold at most 3 elements.
customQueue = deque(maxlen=3)

# Printing the empty deque
print(customQueue)  # Output: deque([])  (empty queue)

# Adding elements one by one to the deque
customQueue.append(1)  # Adds 1
customQueue.append(2)  # Adds 2
customQueue.append(3)  # Adds 3

# Adding a 4th element when maxlen=3 will automatically remove the oldest element (FIFO)
customQueue.append(4)

# Printing deque after appending 4
print(customQueue)  # Output: deque([2, 3, 4], maxlen=3)
# (1 got removed automatically because maxlen is 3)

# Clearing all elements from the deque
print(customQueue.clear())  # Output: None (clear() just empties the deque, doesn't return anything)

# Printing deque after clearing
print(customQueue)  # Output: deque([]) (empty again)
