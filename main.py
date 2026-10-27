
import csv
import shutil
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "transactions.csv"
EXPORT_DIR = BASE_DIR / "exports"

FIELDS = ["date", "type", "category", "amount", "description"]


def initialize():
    EXPORT_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_transactions():
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def add_transaction(transaction_type):
    print(f"\n--- Add {transaction_type.title()} ---")

    date_input = input(
        f"Date (YYYY-MM-DD, Enter for {date.today()}): "
    ).strip()

    if not date_input:
        transaction_date = date.today().isoformat()
    else:
        try:
            transaction_date = datetime.strptime(
                date_input, "%Y-%m-%d"
            ).date().isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

    category = input("Category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = Decimal(input("Amount: ").strip())
        if not amount.is_finite() or amount <= 0:
            print("Amount must be a positive number.")
            return
        amount = amount.quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        print("Please enter a valid amount.")
        return

    description = input("Description (optional): ").strip()

    transaction = {
        "date": transaction_date,
        "type": transaction_type,
        "category": category,
        "amount": str(amount),
        "description": description,
    }

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(transaction)

    print("Transaction saved successfully!")


def view_transactions():
    transactions = load_transactions()

    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n--- All Transactions ---")
    for item in transactions:
        print(
            f"{item['date']} | {item['type'].title()} | "
            f"{item['category']} | {item['amount']} | "
            f"{item['description']}"
        )


def monthly_summary():
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM.")
        return

    transactions = [
        item for item in load_transactions()
        if item["date"].startswith(month)
    ]

    income = sum(
        (Decimal(item["amount"]) for item in transactions
         if item["type"] == "income"),
        Decimal("0")
    )
    expenses = sum(
        (Decimal(item["amount"]) for item in transactions
         if item["type"] == "expense"),
        Decimal("0")
    )

    print(f"\n--- Summary for {month} ---")
    print(f"Total income:   {income:.2f}")
    print(f"Total expenses: {expenses:.2f}")
    print(f"Net balance:    {income - expenses:.2f}")

    category_totals = defaultdict(Decimal)

    for item in transactions:
        if item["type"] == "expense":
            category_totals[item["category"]] += Decimal(item["amount"])

    if category_totals:
        print("\nExpenses by category:")
        for category, total in sorted(category_totals.items()):
            print(f"  {category}: {total:.2f}")

    if not transactions:
        print("No transactions recorded for this month.")


def export_transactions():
    transactions = load_transactions()

    if not transactions:
        print("No transactions available to export.")
        return

    print("\n1. Export to CSV")
    print("2. Export to Excel (.xlsx)")
    choice = input("Choose format: ").strip()

    EXPORT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        output = EXPORT_DIR / f"transactions_{timestamp}.csv"
        shutil.copyfile(DATA_FILE, output)
        print(f"CSV exported to: {output}")

    elif choice == "2":
        try:
            from openpyxl import Workbook
        except ImportError:
            print("Excel export requires openpyxl.")
            print("Install it with: python -m pip install openpyxl")
            return

        output = EXPORT_DIR / f"transactions_{timestamp}.xlsx"
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Transactions"
        sheet.append(FIELDS)

        for item in transactions:
            sheet.append([item[field] for field in FIELDS])

        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions
        workbook.save(output)
        print(f"Excel exported to: {output}")

    else:
        print("Invalid choice.")


def export_chart():
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("Charts require matplotlib.")
        print("Install it with: python -m pip install matplotlib")
        return

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM.")
        return

    totals = defaultdict(Decimal)

    for item in load_transactions():
        if item["date"].startswith(month) and item["type"] == "expense":
            totals[item["category"]] += Decimal(item["amount"])

    if not totals:
        print("No expenses found for this month.")
        return

    EXPORT_DIR.mkdir(exist_ok=True)
    output = EXPORT_DIR / f"expenses_{month}.png"

    categories = list(totals.keys())
    amounts = [float(totals[c]) for c in categories]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts)
    plt.title(f"Expenses by Category - {month}")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

    print(f"Chart saved to: {output}")


def main():
    initialize()

    while True:
        print("\n===== EXPENSE TRACKER CLI =====")
        print("1. Add income")
        print("2. Add expense")
        print("3. View transactions")
        print("4. Monthly summary")
        print("5. Export transactions")
        print("6. Export expense chart")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            export_transactions()
        elif choice == "6":
            export_chart()
        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()

