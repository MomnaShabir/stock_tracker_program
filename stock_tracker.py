
import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400
}

# Store the user's stock information
portfolio = []
total_investment = 0

print("Welcome to the Stock Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input(
        "\nEnter a stock symbol (or 'done' to finish): "
    ).strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity of shares: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        continue

    price = stock_prices[stock_name]
    investment_value = price * quantity

    total_investment += investment_value

    portfolio.append({
        "Stock": stock_name,
        "Quantity": quantity,
        "Price per Share": price,
        "Total Value": investment_value
    })

    print(f"{stock_name}: ${investment_value:.2f}")

# Display the final report
print("\n----- Investment Summary -----")

if portfolio:
    for item in portfolio:
        print(
            f"{item['Stock']} | "
            f"Quantity: {item['Quantity']} | "
            f"Price: ${item['Price per Share']:.2f} | "
            f"Value: ${item['Total Value']:.2f}"
        )

    print(f"\nTotal Investment: ${total_investment:.2f}")

    # Save results to a CSV file
    save_file = input("Save report to CSV? (yes/no): ").strip().lower()

    if save_file == "yes":
        with open("stock_report.csv", "w", newline="") as file:
            fieldnames = [
                "Stock",
                "Quantity",
                "Price per Share",
                "Total Value"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(portfolio)

            writer.writerow({
                "Stock": "TOTAL",
                "Quantity": "",
                "Price per Share": "",
                "Total Value": total_investment
            })

        print("Report saved as stock_report.csv")

else:
    print("No stocks were added to your portfolio.")

print("Thank you for using Stock Tracker!")