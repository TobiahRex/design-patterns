# SOLID
Introduced by Robert C. Martin
1. Single Responsibility Principle
2. Open-Closed Principle
3. Liskov Substitution Principle
4. Interface Segregation Principle
5. Dependency Inversion Principle


# Creational
- Object creation mechanisms, trying to create objects in a manner suitable to the situation.
1. Singleton
2. Factory
3. Abstract Factory
4. Builder
5. Prototype

# Structural
- Object composition: creating relationships between objects to form larger structures.
1. Adapter
2. Bridge
3. Composite
4. Decorator
5. Facade
6. Flyweight
7. Proxy

# Behavioral
- Object to Object communication and how they operate together.
1. Chain of Responsibility
2. Command
3. Interpreter
4. Iterator
5. Mediator
6. Memento
7. Observer
8. State
9. Strategy
10. Template Method
11. Visitor

# Concurrency
1. Monitor Object: Uses an object to synchronize access to a shared resource allowing multiple threas to access the resource safely.
2. Read-Write Lock: Allows multiple threads to read a shared resource simultaneously, but limits access to a single thread when a write operation is being performed.
3. Thread Pool: Creates a pool of worker threads that can be used to execute tasks concrrently.
4. Future: Allows a thread to execute a task asynchronously and provdes a mechanism for the calling thread to retrieve the result at a later time.
5. Producer-Consumer: Allows multiple threads to share common resources with one thread producing data and another consuming it.
6. Guarded Suspension: Allows a thread to wait for a condition to be met before proceeding while still allowing other threads to access shared resources.
7. Two-Phase Termination: Allows a thread to perform cleanup tasks when it is shutting down, while still allowing other threads to access shared resources.
8. Balking: Allows a thread to cancel an operation if a condition is not met, while still allowing other threads to access shared resources. ?
9. Thread-local storage: Allows each thread to have its own private data without the need for explicit synchronization.
10. Double-checked locking: Optimizes the performance of a lock by performing a check before acquiring the lock, in order to avoid unnecessary synchronization.
