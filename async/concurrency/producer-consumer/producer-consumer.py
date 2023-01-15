import threading
import queue

class Producer:
    def __init__(self, queue):
        # Store a reference to the queue
        self.queue = queue

    def run(self):
        # Produce some data
        data = "data"
        # Put the data in the queue
        self.queue.put(data)

class Consumer:
    def __init__(self, queue):
        # Store a reference to the queue
        self.queue = queue

    def run(self):
        # Get the data from the queue
        data = self.queue.get()
        # Consume the data
        print(data)

# Create a queue to store the data
q = queue.Queue()

# Create a producer and a consumer
producer = Producer(q)
consumer = Consumer(q)

# Create threads for the producer and consumer
t1 = threading.Thread(target=producer.run)
t2 = threading.Thread(target=consumer.run)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()
