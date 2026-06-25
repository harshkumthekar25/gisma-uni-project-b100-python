# transaction.py - records every buy and sell

from datetime import datetime 
import csv

class Transaction: 
    """ 
    A transaction records one trade (buy or sell)
    helps keep history of what you did
    """

    all_transactions = [] 

    def __init__(self, stock_symbol, shares, price_per_share, action):
        """
        Creates a transaction record
        """ 
        self.stock_symbol = stock_symbol
        self.shares = shares
        self.price_per_share = price_per_share
        self.action = action
        self.timestamp = datetime.now()
        self.total_value = shares * price_per_share

        # add to class list
        Transaction.all_transactions.append(self)
    
    def __str__(self):
        return f"timestamp = {self.timestamp}"

    def get_stock_symbol(self):
        return self.stock_symbol

    def get_shares(self):
        return self.shares

    def get_total_value(self):
        return self.total_value

    def get_action(self):
        return self.action
    
    @classmethod
    def get_all_transactions(cls):
        return cls.all_transactions

    @classmethod
    def save_all(cls, filename):
        """Saves all transactions to a file"""
        try:
            with open(filename, "w") as file:

                fields = ["times", "action", "stock_symbol", "shares","price_per_share","total_value"]
                csv_writer = csv.DictWriter(file, fieldnames=fields)
                csv_writer.writeheader()
                for t in cls.all_transactions:
                    csv_writer.writerow({
                        "times": t.timestamp,
                        "action": t.action,
                        "stock_symbol": t.stock_symbol,
                        "shares": t.shares,
                        "price_per_share": t.price_per_share,
                        "total_value": t.total_value

                    

                    })

            #file.write("Time, Action, Symbol, Shares, Price, Total\n")
            #for t in cls.all_transactions:
             ###   file.write(f"{t.times},{t.action},{t.stock_symbol},{t.shares},{t.price_per_share},{t._total_value}\n")
                #file.close()
                #return True
        except Exception as exception:
            print("Error saving file!")
            print(exception)
            return False
            

    @classmethod 
    def load_from_file(cls, filename):
        """ Loads transactions from a file"""
        try:
            with open(filename, 'r') as file:
               lines = file.readlines()
            print(f"Loaded {len(lines)-1} transactions")
            return True
        except:
            print("No previous transactions found")
            return False

    def display(self):
       print( f"{self._time.strftime('%H:%M:%S')} - {self.Action} {self.shares} of {self.stock_symbol} for ${self.total_value}")
        
