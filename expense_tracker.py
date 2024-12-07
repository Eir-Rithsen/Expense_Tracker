import argparse
import json
import os
import datetime
from tabulate import tabulate

# File to store expense data
DATA_FILE = "expenses.json"

# Initialize the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)


def load_expenses():
    """Load expenses from the JSON file."""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)


def add_expense(description, amount):
    """Add a new expense."""
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    date = datetime.date.today().isoformat()
    expenses.append({"id": expense_id, "date": date, "description": description, "amount": amount})
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")


def list_expenses():
    """List all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(tabulate(expenses, headers="keys", tablefmt="grid"))


def delete_expense(expense_id):
    """Delete an expense by ID."""
    expenses = load_expenses()
    filtered_expenses = [e for e in expenses if e["id"] != expense_id]
    if len(filtered_expenses) == len(expenses):
        print("Expense ID not found.")
        return
    save_expenses(filtered_expenses)
    print("Expense deleted successfully.")


def update_expense(expense_id, description=None, amount=None):
    """Update an expense."""
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == expense_id:
            if description:
                expense["description"] = description
            if amount:
                expense["amount"] = amount
            save_expenses(expenses)
            print("Expense updated successfully.")
            return
    print("Expense ID not found.")


def summarize_expenses(month=None):
    """Summarize total expenses, optionally for a specific month."""
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        if month:
            expense_month = int(expense["date"].split("-")[1])
            if expense_month != month:
                continue
        total += expense["amount"]
    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")


def export_to_csv(output_file):
    """Export expenses to a CSV file."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses to export.")
        return
    with open(output_file, 'w') as f:
        headers = expenses[0].keys()
        f.write(",".join(headers) + "\n")
        for expense in expenses:
            f.write(",".join(map(str, expense.values())) + "\n")
    print(f"Expenses exported to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker Application")
    subparsers = parser.add_subparsers(dest="command")

    # Add expense
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")

    # List expenses
    subparsers.add_parser("list", help="List all expenses")

    # Delete expense
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument("--id", type=int, required=True, help="ID of the expense to delete")

    # Update expense
    update_parser = subparsers.add_parser("update", help="Update an expense by ID")
    update_parser.add_argument("--id", type=int, required=True, help="ID of the expense to update")
    update_parser.add_argument("--description", help="New description of the expense")
    update_parser.add_argument("--amount", type=float, help="New amount of the expense")

    # Summarize expenses
    summary_parser = subparsers.add_parser("summary", help="Summarize expenses")
    summary_parser.add_argument("--month", type=int, help="Month (1-12) to summarize expenses for")

    # Export expenses to CSV
    export_parser = subparsers.add_parser("export", help="Export expenses to a CSV file")
    export_parser.add_argument("--output", required=True, help="Output CSV file")

    # Parse the arguments
    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "summary":
        summarize_expenses(args.month)
    elif args.command == "export":
        export_to_csv(args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
