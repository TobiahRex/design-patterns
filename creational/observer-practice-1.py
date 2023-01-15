import abc

class ObsrvSubject(metaclass=abc.ABCMeta):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class Stock(ObsrvSubject):
    def __init__(self, symbol, price):
        super().__init__()
        self.symbol = symbol
        self.price = price

    def set_price(self, price):
        self.price = price
        self.notify() # notify all observers of this Subject (stock symbol)


class Observer(metaclass=abc.ABCMeta):
    """The purpose is to define an update() method
    that is called when the Subject changes.

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.
    """
    @abc.abstractmethod
    def update(self):
        pass

class Investor(Observer):
    def __init__(self, name, stock: Stock):
        super().__init__()
        self.stock = stock
        self.name = name
        self.stock.attach(self) # attach this observer to the Subject (stock symbol)

    def update(self):
        print(f"{self.name}: The price of {self.stock.symbol} has changed to ${self.stock.price}")

google = Stock("GOOG", 1000)
investor1 = Investor("John", google)
investor2 = Investor("Mike", google)

google.set_price(1100)  # Outputs: "John: The price of GOOG has changed to $1100" and "Jane: The price of GOOG has changed to $1100"
google.set_price(900) # Outputs: "John: The price of GOOG has changed to $900" and "Jane: The price of GOOG has changed to $900"
