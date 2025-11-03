#C:\Users\window 11\Desktop\dsa\DSA-2025\Queue\MultiprocessingQueue.py
# Importing Queue from the multiprocessing module
# This Queue is used when you want to share data between multiple processes
# (different programs running in parallel).
from multiprocessing import Queue

# Creating a Queue object with a maximum size of 3
customQueue = Queue(maxsize=3)

# Adding (enqueue) an element into the queue
customQueue.put(1)  # Puts 1 into the queue

# Removing (dequeue) the first element from the queue
print(customQueue.get())  # Output: 1 (FIFO - first in, first out)
