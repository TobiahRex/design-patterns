import threading

class GuardedResource:
    def __init__(self):
        self.mutex = threading.Lock()
        self.cond = threading.Condition(self.mutex)
        self.resource = None

    def wait_for_resource(self):
        with self.cond:
            # Wait for the resource to become available
            self.cond.wait_for(lambda: self.resource is not None)
            # Use the resource
            print(f'Using resource: {self.resource}')

    def set_resource(self, resource):
        with self.cond:
            # Set the resource
            self.resource = resource
            # Notify any waiting threads that the resource is available
            self.cond.notify_all()

# Create an instance of the GuardedResource class
resource = GuardedResource()

# Wait for the resource to become available
resource.wait_for_resource()

# Set the resource
resource.set_resource('My Resource')

"""
In this example, the GuardedResource class has a wait_for_resource method that waits for the
resource attribute to become available, and a set_resource method that sets the resource
attribute and notifies any waiting threads that the resource is available. The wait_for_resource
method uses the wait_for method of the Condition object to wait for the condition (that the
resource attribute is not None) to be satisfied.
"""