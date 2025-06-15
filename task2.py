import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Dictionary: {symbol: shares}

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares
        print(f"✅ Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"🗑️ Removed {symbol} from your portfolio.")
        else:
            print(f"⚠️ {symbol} not found in portfolio.")

    def get_stock_price(self, symbol):
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
        try:
            response = requests.get(url)
            data = response.json()
            return data['quoteResponse']['result'][0]['regularMarketPrice']
        except Exception:
            return None

    def show_portfolio(self):
        if not self.portfolio:
            print("📭 Your portfolio is empty.")
            return

        print("\n📊 Portfolio Overview:")
        total_value = 0.0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is None:
                print(f"{symbol}: ❌ Price not available.")
                continue
            value = shares * price
            total_value += value
            print(f"{symbol}: {shares} shares × ${price:.2f} = ${value:.2f}")
        print(f"💰 Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()
    while True:
        print("📈 STOCK PORTFOLIO TRACKER")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ")
            try:
                shares = int(input("Enter number of shares: "))
                portfolio.add_stock(symbol, shares)
            except ValueError:
                print("❌ Invalid number of shares.")
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            print("👋 Exiting. Have a nice day!")
            break
        else:
            print("❌ Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()
