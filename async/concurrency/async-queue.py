import threading

class AsyncQueue:
    def __init__(self):
        # Create a lock object to synchronize access to the queue
        self.lock = threading.Lock()
        # Create a condition object to signal the availability of data in the queue
        self.cond = threading.Condition(self.lock)
        # Create an empty list to store the data
        self.data = []

    def put(self, item):
        # Acquire the lock
        with self.lock:
            # Add the item to the queue
            self.data.append(item)
            # Notify any waiting threads that data is available
            self.cond.notify()

    def get(self):
        # Acquire the lock
        with self.lock:
            # Wait for data to be available
            self.cond.wait_for(lambda: self.data)
            # Remove the first item from the queue
            item = self.data.pop(0)
            # Return the item
            return item

# Create an instance of the AsyncQueue class
q = AsyncQueue()

# Put some data in the queue
q.put("data1")
q.put("data2")

# Get the data from the queue
print(q.get())
print(q.get())

"""
The wait_for method of the Condition class is used to block the current thread until a specific
condition is met. In this case, the condition is specified as a lambda function that returns the
value of self.data, which is a list that stores the data in the queue. If the list is empty, the
lambda function will return False, and the thread will block until the condition becomes True.
If the list is non-empty, the lambda function will return True, and the thread will continue executing.

In other words, the wait_for method is used to wait for data to become available in the queue.
When data is added to the queue by a producer, the put method will call the notify method of
the Condition object to signal that data is available, and any waiting threads will be unblocked and able to retrieve the data from the queue.
"""