print("==================================")
print("            Stock Portfolio Tracker         ")
print("===============================================")
print("Welcome to our portfolio tracker")
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200,
}
portfolio = {}
total_value = 0
while True:
    stock = input("\nEnter stock symbo: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("invalid stock symbol")
        continue
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid quantity")
        continue
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity
    #calculate investment
    price = stock_prices[stock]
    investment = price * quantity
    print("\nStock: ", stock)
    print("Quantity: ", quantity)
    print("Price per share: ", price)
    print("Investment: ", investment)
    #portfolio summary
    print("\n==========================")
    print("========Portfolio Summary========")
    total_value = 0
    #Display all stocks
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        print("\nStock: ", stock)
        print("Quantity: ", quantity)
        print("Price per share: ", price)
        print("Total value: ", value)
        total_value += value
    #Display total
    print("\n======================")
    print("Total portfolio value: ", total_value)
    print("------------------------")
    # save portfolio to a file
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares, total value: {value}\n")
        file.write(f"Total portfolio value: {total_value}\n")
        print("\nportfolio saved successfully")
        

