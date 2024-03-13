import requests

# Make a class for the stock
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

# Function to add a stock
    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

# Function to remove a stock if found
    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print("done")
            else:
                self.portfolio[symbol] -= quantity
                print("DONE")
        else:
          print("Symbol you entered not in stock")

# Function to get the value of portfolio 
    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            total_value += price * quantity
        return total_value

    def get_stock_price(self, symbol):
        api_key = '7R06XYA757YBKYFG'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return float(data['Global Quote']['05. price'])


# make instance
portfolio_obj = StockPortfolio()

# main function to start the program
def main():
  print("Welcome in the stock portfolio")
  print("To add press 1")
  print("To remove press 2")
  print("To get portfolio value press 3")
  print("To exit press 0")

  
  while True: 
    print("Enter your choice: ")
    choice= input()
    if choice=="1":
      print("Enter the symbol to be added: ")
      symbol_for_add=input()
      print("Enter the quantity: ")
      quantity_for_add=int(input())
      portfolio_obj.add_stock(symbol_for_add, quantity_for_add)
      print("Added")
    
    elif choice=="2":
      print("Enter the symbol to be removed: ")
      symbol_for_remove=input()
      print("Enter the quantity: ")
      quantity_for_remove=int(input())
      portfolio_obj.remove_stock(symbol_for_remove, quantity_for_remove)

    elif choice=="3":
      print("Portfolio Value:", portfolio_obj.get_portfolio_value())
      
    elif choice=="0":
      print("Happy for helping you")
      break
    
    else:
      print("invalid input please try again")
      
# Run the program
if __name__ == "__main__":
  main()