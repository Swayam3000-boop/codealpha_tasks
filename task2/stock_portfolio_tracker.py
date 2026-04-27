import csv
import os
from datetime import datetime

# ---------- Hardcoded stock price dictionary ----------
STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  185,
    "MSFT":  415,
    "META":  500,
    "NFLX":  620,
    "NVDA":  900,
}


def display_available_stocks():
    """Print all available stocks with their prices."""
    print("\n" + "=" * 40)
    print("  Available Stocks")
    print("=" * 40)
    print(f"  {'Ticker':<10} {'Price (USD)':>12}")
    print("-" * 40)
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<10} ${price:>11,.2f}")
    print("=" * 40)


def get_portfolio_from_user():
    """Prompt user to enter stock names and quantities."""
    portfolio = {}   # { ticker: quantity }

    print("\nEnter your stock holdings.")
    print("Type 'done' when finished.\n")

    while True:
        ticker = input("Stock ticker (e.g. AAPL): ").strip().upper()

        if ticker == "DONE":
            break

        if ticker not in STOCK_PRICES:
            print(f"  ⚠  '{ticker}' not found. Available: {', '.join(STOCK_PRICES)}\n")
            continue

        try:
            qty = int(input(f"  Quantity of {ticker}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive integer.\n")
                continue
        except ValueError:
            print("  ⚠  Please enter a whole number.\n")
            continue

        # Accumulate if the same ticker is entered more than once
        portfolio[ticker] = portfolio.get(ticker, 0) + qty
        print(f"  ✔  Added {qty} × {ticker}\n")

    return portfolio


def calculate_portfolio(portfolio):
    """Return a list of (ticker, qty, price, value) rows and the grand total."""
    rows = []
    total = 0.0
    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * qty
        total += value
        rows.append((ticker, qty, price, value))
    return rows, total


def display_results(rows, total):
    """Pretty-print the portfolio summary."""
    print("\n" + "=" * 55)
    print("  Portfolio Summary")
    print("=" * 55)
    print(f"  {'Stock':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}")
    print("-" * 55)
    for ticker, qty, price, value in rows:
        print(f"  {ticker:<8} {qty:>6}  ${price:>9,.2f}  ${value:>11,.2f}")
    print("=" * 55)
    print(f"  {'TOTAL INVESTMENT':.<38} ${total:>11,.2f}")
    print("=" * 55)


def save_results(rows, total):
    """Ask user whether to save results, then save as .txt or .csv."""
    print("\nWould you like to save the results?")
    print("  1 → Save as .txt")
    print("  2 → Save as .csv")
    print("  3 → Skip")

    choice = input("Your choice (1/2/3): ").strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 55 + "\n")
            f.write(f"{'Stock':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}\n")
            f.write("-" * 55 + "\n")
            for ticker, qty, price, value in rows:
                f.write(f"{ticker:<8} {qty:>6}  ${price:>9,.2f}  ${value:>11,.2f}\n")
            f.write("=" * 55 + "\n")
            f.write(f"Total Investment: ${total:,.2f}\n")
        print(f"\n  ✔  Saved as '{filename}'")

    elif choice == "2":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Value (USD)"])
            for ticker, qty, price, value in rows:
                writer.writerow([ticker, qty, price, value])
            writer.writerow([])
            writer.writerow(["Total", "", "", total])
        print(f"\n  ✔  Saved as '{filename}'")

    else:
        print("\n  Results not saved.")


# ─────────────────────────  Main program  ─────────────────────────

def main():
    print("\n╔══════════════════════════════════════╗")
    print("║    📈  Stock Portfolio Tracker       ║")
    print("╚══════════════════════════════════════╝")

    display_available_stocks()

    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("\n  No stocks entered. Exiting.")
        return

    rows, total = calculate_portfolio(portfolio)
    display_results(rows, total)
    save_results(rows, total)

    print("\nThank you for using the Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()
