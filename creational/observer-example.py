import abc

class Subject(metaclass=abc.ABCMeta):
  """The subject interface."""

  def __init__(self):
    self.observers = []

  def attach(self, observer):
    """Attach an observer to the subject."""
    self.observers.append(observer)

  def detach(self, observer):
    """Detach an observer from the subject."""
    self.observers.remove(observer)

  def notify(self):
    """Notify all observers."""
    for observer in self.observers:
      observer.update()

class Observer(metaclass=abc.ABCMeta):
  """The observer interface."""

  @abc.abstractmethod
  def update(self):
    pass

class Stock(Subject):
  """A stock subject."""

  def __init__(self, symbol, price):
    super().__init__()
    self.symbol = symbol
    self.price = price

  def set_price(self, price):
    """Set the price of the stock."""
    self.price = price
    self.notify()

class Investor(Observer):
  """An investor observer."""

  def __init__(self, name, stock):
    self.name = name
    self.stock = stock
    self.stock.attach(self)

  def update(self):
    """Update the investor."""
    print(f"{self.name}: The price of {self.stock.symbol} has changed to ${self.stock.price}")

# Example usage

stock = Stock("GOOG", 1000)
investor1 = Investor("John", stock)
investor2 = Investor("Jane", stock)

stock.set_price(1100)  # Outputs: "John: The price of GOOG has changed to $1100" and "Jane: The price of GOOG has changed to $1100"
stock.set_price(900)   # Outputs: "John: The price of GOOG has changed to $900" and "Jane: The price of GOOG has changed to $900"
"""

In this example, we have a Subject interface and a Stock class that implements the Subject interface.
The Stock class maintains a list of Observer objects and provides methods to attach and detach observers to the subject.
The notify method is used to send a notification to all attached observers when the state of the subject changes.

We also have an Observer interface and an Investor class that implements the Observer interface.
The Investor class is notified when the state of the Stock object changes and updates itself accordingly.

In this example, we can use the Stock and Investor classes to create a simple stock tracking system.
When the price of the stock changes, the Stock object sends a notification to all attached investors, who update themselves with the new price.

The Observer pattern allows us to create a flexible system where the state of one object can be automatically propagated to multiple other objects,
without the objects being explicitly aware of each other.
"""