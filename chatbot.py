import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": str(datetime.now().date())
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\n✅ Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found!")
        return

    print("\n------ Expense History ------")

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Amount: ₹", expense["amount"])

        total += expense["amount"]

    print("\n----------------------------")
    print("Total Expense: ₹", total)


def search_expense(expenses):
    category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("\n", expense)
            found = True

    if not found:
        print("No expense found for this category.")


def main():

    expenses = load_expenses()

    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expense(expenses)

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
