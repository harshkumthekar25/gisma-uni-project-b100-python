# stock.py - defines what a stock is

class Stock:
    """ 
    A stock represents ownership in one company.
    Example: Apple stock with symbol AAPL
    """

    def __init__(self, symbol, company_name, current_price):
        """
        Creates a new stock with symbol , company name and price """
        self.symbol = symbol
        self.company_name = company_name
        self.current_price = current_price

        # Getter methods (like asking "What is your name?")
    def get_symbol(self):
           return self.symbol

    def get_company_name(self):
        return self.company_name

    def get_current_price(self):
        return self.current_price

        # Setter method (like changing the price)
    def set_current_price(self, new_price):
        """
        Updates the stock price
        Only accepts positive numbers
        """
        if new_price > 0:
            self.current_price = new_price
        else:
            print("Price must be positive!")

    def display(self):
        print(f"{self.symbol}: {self.company_name} - ${self.current_price}")
