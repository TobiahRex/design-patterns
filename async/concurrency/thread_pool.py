import concurrent.futures
import os

def task(n):
  return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count(), min_workers=2) as executor:
  for i in range(10):
    result = executor.submit(task, i)
    print(result.result())

    """
    In this example, the ThreadPoolExecutor is created with an upper bound of 4 worker threads
    (the number of available CPUs on the machine) and a lower bound of 2 worker threads.
    The for loop submits 10 tasks to the thread pool, and the result.result() method is used
    to print the result of each task.

    I hope this helps to illustrate how you can specify the upper and lower bound number of workers
    for a ThreadPoolExecutor in Python. Let me know if you have any further questions.
    """