import concurrent.futures
import threading
import psycopg2

class Database:
    def __init__(self, host, database, user, password):
        # Connect to the database
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        # Create a cursor object
        self.cursor = self.conn.cursor()
        # Create a lock object to synchronize access to the database
        self.lock = threading.RLock()

    def read(self):
        # Acquire the lock in shared mode
        with self.lock:
            # Execute a SELECT query to retrieve data from the database
            self.cursor.execute("SELECT * FROM table")
            # Fetch the results of the query
            rows = self.cursor.fetchall()
            # Iterate over the rows and print the data
            for row in rows:
                print(row)

    def write(self, data):
        # Acquire the lock in exclusive mode
        with self.lock:
            # Execute an INSERT query to write data to the database
            self.cursor.execute("INSERT INTO table (column) VALUES (%s)", (data,))
            # Commit the transaction to persist the data
            self.conn.commit()

    def close(self):
        # Close the cursor and connection
        self.cursor.close()
        self.conn.close()

# Create an instance of the Database class
db = Database(host="localhost", database="mydatabase", user="user", password="password")

# Create a thread pool with 4 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit a task to read from the database
    task1 = executor.submit(db.read)
    # Submit a task to write to the database
    task2 = executor.submit(db.write, "data")
    # Wait for the tasks to complete
    concurrent.futures.wait([task1, task2])

# Close the database connection
db.close()
