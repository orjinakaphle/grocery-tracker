# grocery_tracker.py
#required imports
import csv
from datetime import datetime #Imports the datetime class to work with the current date.
import matplotlib.pyplot as plt #Imports the plotting module matplotlib.pyplot as plt, which is used to create graphs.

def add_expense(): #function add expense
    category = input("Enter category (e.g., Fruits, Drinks, Stationaries, Fees): ").strip()
    amount = float(input("Enter amount spent: "))
    date = datetime.now().strftime('%Y-%m-%d')
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!\n")

def show_expenses(): #function show expense
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nDate\t\tCategory\tAmount")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t${row[2]}")
    except FileNotFoundError:
        print("No expense records found.\n")

def plot_expenses(): #function to generate a bar chart of spending by category.
    categories = {}
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                cat = row[1]
                amt = float(row[2])
                categories[cat] = categories.get(cat, 0) + amt
        if not categories:
            print("No data to plot.\n")
            return
        plt.bar(categories.keys(), categories.values())
        plt.title("Grocery Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No data file found. Please add expenses first.\n")

def menu(): #The function that shows the main menu and handles use input
    while True:
        print("==== Grocery Tracker ====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Plot Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            plot_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
