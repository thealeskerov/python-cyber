# Simple expense tracker that stores data in a CSV file

import csv

def add_expense():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added.")

def view_total():
    total = 0
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"Total expenses: {total} PLN")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Menu loop
while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View total")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_total()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
