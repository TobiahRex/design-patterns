# Concurrency
1. **Monitor Object**: Uses an object to synchronize access to a shared resource allowing multiple threas to access the resource safely.
    - Mental Model: locking the kitchen while you cook, not letting anyone else into the kitchen. Once you're finished you re-open the kitchen and let someone else in.
    - Code
        ```python
        class MonitorObject:
            def __init__(self):
                self.lock = threading.Lock()
                self.resource = SharedResource()

            def do_something(self):
                # Acquire the lock
                with self.lock:
                    # Perform some operation on the shared resource
                    self.resource.perform_operation()
                # Release the lock
        ```
    - Python's `lock`
        ```python
        import threading

        lock = threading.Lock()

        # Acquire the lock
        lock.acquire()

        # Perform some operation on a shared resource
        shared_resource.do_something()

        # Release the lock
        lock.release()
        ```
    - Python's Context Management using `with`
        ```python
        lock = threading.Lock()

        with lock:
            # Perform some operation on a shared resource
            shared_resource.do_something()

        # The lock is automatically released when the with block is exited
        ```
2. **Read-Write Lock**: Allows multiple threads to read a shared resource simultaneously, but limits access to a single thread when a write operation is being performed.
    - Mental Model: A community workshop is accessed by multiple people at the same time. When the workshop needs to be renovated then the workshop is locked and nobody else can enter the workshop. Once the workshop is finished being renovated, it's re-opened and other people can access it.
    - Code
        ```python
        import threading
        class ReadWriteLock:
            def __init__(self):
                self.read_lock = threading.Lock()
                self.write_lock = threading.Lock()
                self.readers = 0

            def acquire_read(self):
                # Acquire the read lock
                self.read_lock.acquire()
                self.readers += 1
                if self.readers == 1:
                    # If this is the first reader, acquire the write lock
                    self.write_lock.acquire()
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
        ```
3. **Thread Pool**: Creates a pool of worker threads that can be used to execute tasks concrrently.
4. Future: Allows a thread to execute a task asynchronously and provdes a mechanism for the calling thread to retrieve the result at a later time.
5. **Producer-Consumer**: Allows multiple threads to share common resources with one thread producing data and another consuming it.
6. **Guarded Suspension**: Allows a thread to wait for a condition to be met before proceeding while still allowing other threads to access shared resources.
7. **Two-Phase Termination**: Allows a thread to perform cleanup tasks when it is shutting down, while still allowing other threads to access shared resources.
8. **Balking**: Allows a thread to cancel an operation if a condition is not met, while still allowing other threads to access shared resources. ?
9. **Thread-local storage**: Allows each thread to have its own private data without the need for explicit synchronization.
10. **Double-checked locking**: Optimizes the performance of a lock by performing a check before acquiring the lock, in order to avoid unnecessary synchronization.
