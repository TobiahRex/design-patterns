import redis

class RedisCluster:
    def __init__(self):
        # Create a Redis connection pool for each node in the cluster
        self.node1 = redis.ConnectionPool(host='node1.example.com', port=6379)
        self.node2 = redis.ConnectionPool(host='node2.example.com', port=6379)
        self.node3 = redis.ConnectionPool(host='node3.example.com', port=6379)

    def get_connection(self, key):
        # Calculate the hash of the key to determine which node it belongs to
        hash_value = hash(key)
        # Choose a node based on the hash value
        if hash_value % 3 == 0:
            return redis.Redis(connection_pool=self.node1)
        elif hash_value % 3 == 1:
            return redis.Redis(connection_pool=self.node2)
        else:
            return redis.Redis(connection_pool=self.node3)

    def set(self, key, value):
        # Get a connection to the appropriate node
        r = self.get_connection(key)
        # Set the value in Redis
        r.set(key, value)

    def get(self, key):
        # Get a connection to the appropriate node
        r = self.get_connection(key)
        # Get the value from Redis
        return r.get(key)

# Create an instance of the RedisCluster class
cluster = RedisCluster()

# Set a value in the cluster
cluster.set("key1", "value1")

# Get the value from the cluster
print(cluster.get("key1"))

"""
In this example, the RedisCluster class has a set method and a get method that allow you to store and
retrieve data from the Redis cluster. The get_connection method is used to determine which node in
the cluster a key belongs to based on the hash of the key. The set method uses the get_connection
method to get a connection to the appropriate node, and then uses the set method of the redis module
to store the value in Redis. The get method uses the get_connection method to get a connection to the
appropriate node, and then uses the get method of the redis module to retrieve the value from Redis.
"""