#C:\Users\window 11\Desktop\dsa\DSA-2025\Queue\QueueModule.py

# Importing Python's built-in queue module and giving it an alias 'q'
import queue as q

# Creating a Queue object with a maximum size of 3
customQueue = q.Queue(maxsize=3)

# Checking if the queue is empty (returns True if empty, False if not)
print(customQueue.empty())  # Output: True (because we haven't added anything yet)

# Adding (enqueue) elements to the queue
customQueue.put(1)  # Adds 1 to the queue
customQueue.put(2)  # Adds 2 to the queue
customQueue.put(3)  # Adds 3 to the queue

# Checking if the queue is full (returns True if it reached max size)
print(customQueue.full())  # Output: True (because we added 3 items, which is maxsize)

# Removing (dequeue) the first element from the queue
print(customQueue.get())  # Output: 1 (FIFO - first in, first out)

# Checking how many elements are still in the queue
print(customQueue.qsize())  # Output: 2 (because we removed one element)
