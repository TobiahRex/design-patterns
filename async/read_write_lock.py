import threading

class ReadWriteLock:
    def __init__(self):
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock()
        self.readers = 0

    def acquire_read(self):
        """If the reader is the first instance, then we want to immediately grab the write lock. The idea
        here is that we should assume that write ability is granted to the first instance of the shared
        resource. If multiple threads want to write to the shared resource, then only the first instance
        has the ability to write. Other instances could be granted the ability to write but only after
        the first instance calls `write_lock.release()`.
        """
        # Acquire the read lock
        self.read_lock.acquire()
        self.readers += 1
        if self.readers == 1:
            self.acquire_write() # If this is the first reader, acquire the write lock
        # Release the read lock
        self.read_lock.release()

    def release_read(self):
        # Acquire the read lock
        self.read_lock.acquire()
        self.readers -= 1
        if self.readers == 0:
            # If this is the last reader, release the write lock
            self.write_lock.release()
        # Release the read lock
        self.read_lock.release()

    def acquire_write(self):
        # Acquire the write lock
        self.write_lock.acquire()

    def release_write(self):
        # Release the write lock
        self.write_lock.release()

class SharedResource:
    def __init__(self):
        self.data = []
        self.lock = ReadWriteLock()

    def read_data(self):
        # Acquire the read lock
        self.lock.acquire_read()
        # Perform some operation on the data
        print(self.data)
        # Release the read lock
        self.lock.release_read()

    def write_data(self):
        # Acquire the write lock
        self.lock.acquire_write()
        # Perform some operation on the data
        self.data.append(1)
        # Release the write lock
        self.lock.release_write()

def worker_thread(resource):
    # Do some work with the shared resource
    resource.read_data()
    resource.write_data()


# Create a shared resource
resource = SharedResource()

# Create some threads
threads = [threading.Thread(target=worker_thread, args=(resource,)) for _ in range(10)]

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to finish
for thread in threads:
    thread.join() # blocks the calling thread by joining all worker threads together

# Do some more work with the shared resource
resource.read_data()
resource.write_data()