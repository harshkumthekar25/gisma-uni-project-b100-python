"""
Portfolio Class - Holds all stocks a user owns
Like a shopping cart but for stocks
"""

class Portfolio:
    """ 
    A portfolio keeps track of which stocks you own and how many shares of each"""

    def __init__(self, owner_name):
        """
        Creates an empty portfolio for a user
        """
        self.owner_name = owner_name
        self.holdings = {} #dictionary : stock_symbol -> number of shares
        self.cash_balance = 10000.00 # start with 10,000 demo cash

    def get_owner_name(self):
        """" Returns owner name """
        return self.owner_name

    def get_cash_balance(self):
        """ Returns cash balance"""
        return self.cash_balance
        
    def buy(self, stock, shares):
        "Buy shares of a stock if you have enough money"
        cost = stock.get_current_price() * shares
        if cost <= self.cash_balance:
            self.cash_balance -= cost
            symbol = stock.get_symbol()
            if symbol in self.holdings:
                self.holdings[symbol] = self.holdings[symbol] + shares
            else:
                self.holdings[symbol] = shares
            return True
        else:
            return False

    def sell(self, stock, shares):
        symbol = stock.get_symbol()
        if symbol in self.holdings and self.holdings[symbol] >= shares:
           value = stock.get_current_price() * shares 
           self.cash_balance = self.cash_balance+ value 
           self.holdings[symbol] = self.holdings[symbol] - shares
           del self.holdings[symbol]
           return True
        
    

    def show(self): 
        """ Print your Portfolio"""
        print("\n" + "=" *40)
        print(f"Portfolio of {self.owner_name}")
        print(f"Cash: ${self.cash_balance:.2f}")
        print("Stocks owned:")
        if len(self.holdings) == 0:
            print("  None")
        else:
            for symbol, shares in self.holdings.items():
                print(f" {symbol}: {shares} shares")
        print("="*40) 


    

      
        
        
    