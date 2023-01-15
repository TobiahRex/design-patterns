import threading
import psycopg2

# Create a lock object to synchronize access to the database
lock = threading.Lock()

# Define a function for reading from the database
def read_from_db(conn, cursor):
    # Acquire the lock to synchronize access to the database
    with lock:
        # Execute a SELECT query to retrieve data from the database
        cursor.execute("SELECT * FROM table")
        # Fetch the results of the query
        rows = cursor.fetchall()
        # Iterate over the rows and print the data
        for row in rows:
            print(row)

# Define a function for writing to the database
def write_to_db(conn, cursor, data):
    # Acquire the lock to synchronize access to the database
    with lock:
        # Execute an INSERT query to write data to the database
        cursor.execute("INSERT INTO table (column) VALUES (%s)", (data,))
        # Commit the transaction to persist the data
        conn.commit()

# Connect to the database
conn = psycopg2.connect(host="localhost", database="mydatabase", user="user", password="password")
# Create a cursor object
cursor = conn.cursor()

# Create a thread to read from the database
thread1 = threading.Thread(target=read_from_db, args=(conn, cursor))
# Create a thread to write to the database
thread2 = threading.Thread(target=write_to_db, args=(conn, cursor, "data"))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Close the cursor and connection
cursor.close()
conn.close()
