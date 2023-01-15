"""
You are building a stock trading application that allows users to track the prices of their favorite stocks.
The application has a "Stock" class that represents a stock and a "Portfolio" class that represents a user's collection of stocks.
The Portfolio class needs to be notified whenever the price of a stock in the portfolio changes so that it can update the user's portfolio balance.
"""
import abc

class Observer(metaclass=abc.ABC):
    @abc.abstractmethod
    def update():
        pass

class Observable(abc.ABC):
    def __init__(self) -> None:
        self.observers = []

    def observe(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Stock(Observable):
    def __init__(self, symbol, purchase_price):
        self.symbol = symbol
        self.price = purchase_price
        self.purchase_price = purchase_price

    def set_price(self, price):
        self.price = price
        self.notify_observers()

class Portfolio(Observer):
    def __init__(self, balance):
        self.balance = balance
        self.stocks = []

    def add(self, stock: Stock, quantity):
        self.stocks[stock.symbol] = quantity
        self.observe(stock)

    def update(self, stock):
        self.balance += self.stocks[stock.price] * (stock.price - stock.purchase_price)


google = Stock('GOOGLE', purchase_price=1000)
portfolio = Portfolio(10000)
portfolio.add(google, 10)
google.set_price(1100)