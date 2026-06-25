"""
Main Trading Application 
This is where the user interacts with the program
Like the "game menu" when you press buttons
"""

import time
from stock import Stock
from portfolio import Portfolio
from transaction import Transaction


def display_menu():
    """ shows the menu option to user"""
    print("\n" + "=" *50)
    print("     CAPITAL.COM TRADING SIMULATOR")
    print("=" *50)
    print("1. View Availale Stocks")
    print("2. View my Portfolio")
    print("3. Buy Stocks")
    print("4. Sell Stocks")
    print("5. View Transaction History")
    print("6. Save Transactions")
    print("7. Save and close")
    print("=" *50)

def get_stocks():
    """Create 4 simple stocks to trade"""
    stocks = [
        Stock("AAPL", "Apple Inc.", 175.50),
        Stock("GOOGL", "Alphabet (Google)", 138.25),
        Stock("MSFT", "Microsoft", 330.50),
        Stock("TSLA", "Tesla Inc.", 245.75),
        Stock("AMZN", "Amazon.com", 145.80)

    ]
    return stocks

def display_stocks(stocks):
    """ shows all available stocks with prices"""
    print("\n --- Available stocks ---")
    for i, s in enumerate(stocks,1):
        print(f"{i}. {s.symbol}: {s.company_name} - ${s.current_price}")
    print("----------------------")

    
def main():
    """ Main function that runs the trading simulator"""
    
    print("\n  Welcome to Capital.com trading simulator! ")
    print(" You start with $10,000 virtual cash to practice trading.\n")
    
    user_name = input("what is your name? ")


    # Create portfolio for user
    my_portfolio = Portfolio(user_name)

    # Load available stocks
    all_stocks = get_stocks()

    # load previous transactions if any
    Transaction.load_from_file("transactions.csv")

    running = True

    while running:
        display_menu()
        choice = input ("\nEnter your choice (1-7): ")

        #Menu option 1: View Stocks
        if choice == "1":
            display_stocks(all_stocks)
            input("\nPress enter to continue...")

        #Menu option 2: View Portfolio
        elif choice == "2":
            my_portfolio.show()
            input("Press enter to continue...")

        #Menu option 3: Buy Stocks
        elif choice == "3":
            display_stocks(all_stocks)

            try:
                stock_num = int(input("\nWhich stock number do you want to buy? "))
                #stock = get_stocks(all_stocks, stock_num)
                stock = all_stocks[stock_num - 1]

                if stock:
                    shares = int(input(f"How many shares of {stock.get_symbol()}? "))

                    if shares > 0:
                        success = my_portfolio.buy(stock, shares)

                        if success:
                            # Create a transaction record
                            trans = Transaction(stock.get_symbol(), shares, stock.get_current_price(), "BUY")

                            print(f"\nBOUGHT {shares} shares of {stock.get_symbol()}!")

                            print(f"Remaining cash: ${my_portfolio.get_cash_balance():,.2f}")

                        else:
                            print(f"\n Not enough cash! You need ${shares * stock.get_current_price():,.2f}")

                    else:
                        print(" Shares must be positive!")
                else:
                    print(" Invalid stock choice!")

            except:
                print(" Please enter Numbers only")

            input("\nPress enter to continue...")

        #Menu option 4: Sell Stocks
        elif choice == "4":
            my_portfolio.show()

            if my_portfolio.holdings:
                try:
                    sell_symbol = input("\nEnter stock symbol to sell(e.g., AAPL): ").upper()

                    if sell_symbol in my_portfolio.holdings:
                        shares_owned = my_portfolio.holdings[sell_symbol]
                        shares = int(input(f"You own {shares_owned} shares. How many to sell? "))


                        if 0 < shares <= shares_owned:
                            #find the stock object
                            stock_to_sell = None
                            for s in all_stocks:
                                if s.get_symbol() == sell_symbol:
                                    stock_to_sell = s
                                    break

                            if stock_to_sell:
                                success = my_portfolio.sell(stock_to_sell, shares)

                                if success: 
                                    trans = Transaction(sell_symbol, shares, stock_to_sell.get_current_price(), "SELL")
                                    print(f"\n SOLD {shares} shares of {sell_symbol}!")
                                    print(f" New Cash balance: ${my_portfolio.get_cash_balance():,.2f}")
                                else:
                                    print("Could not sell")
                            else:
                                print("Invalid number of shares")
                        else:
                            print (f" You don't own {sell_symbol}")
                    else:
                        print(sell_symbol)
                        print(my_portfolio.holdings)
                        
                except Exception as exception:
                    print(f"An error occured: {exception}")

            else:
                print("You don't own any stocks yet!")

            input("\nPress enter to continue...")

        #menu option 5: Viewing saving and closing
        elif choice == "5" or "6" or "7":

            all_trans = Transaction.get_all_transactions()
            print("\n" + "=" * 50)
            print("TRANSACTION HISTORY")
            print("=" *50)

            if len(all_trans) == 0:
                print("No transactions yet!")
            else: 
                for t in all_trans:
                    print(t)
                print("=" *50)
                input("\nPress Enter to continue...")

            #Menu option 6: Save transactions and save and close
            if choice == "6" or "7":
                print("\n Saving your transactions...")
                Transaction.save_all("transactions.csv")
                print(" Saved! Thanks for trading with Capital.com!")
                print("Remember: This is practice trading, not real money!")
                if choice == "7":
                   running = False
            

        else:
            print(" Invalid choice! Please enter 1-7")
            time.sleep(1)

if __name__ == "__main__":
    
    main()