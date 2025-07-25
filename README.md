# Grocery Tracker

`grocery_tracker.py` is a simple command-line application that allows you to track grocery expenses, view past expenses, and visualize spending trends using a bar chart.

---

## **Features**

* **Add Expense**: Record your daily grocery expenses with category, amount, and date.
* **Show Expenses**: View all recorded expenses in a tabular format.
* **Plot Expenses**: Generate a bar chart visualization of total spending by category.
* **Persistent Storage**: All data is stored in `expenses.csv` for future use.

---

## **Requirements**

Before running the program, ensure you have the following installed:

* **Python 3.x**
* Required Python libraries:

  ```bash
  pip install matplotlib
  ```

---

## **How to Use**

1. **Run the Program**

   ```bash
   python grocery_tracker.py
   ```

2. **Menu Options**

   * **1. Add Expense**
     Add a new expense by entering a category (e.g., Fruits, Drinks) and amount spent.
   * **2. Show Expenses**
     Display all recorded expenses from the `expenses.csv` file.
   * **3. Plot Expenses**
     Generate a bar chart showing total spending per category.
   * **4. Exit**
     Exit the program.

---

## **File Structure**

* **grocery\_tracker.py** – Main Python script.
* **expenses.csv** – Stores expenses in the format:

  ```
  Date,Category,Amount
  ```
* **README.md** – Documentation for the project.

---

## **Example Usage**

**Adding an Expense:**

```
==== Grocery Tracker ====
1. Add Expense
2. Show Expenses
3. Plot Expenses
4. Exit
Choose an option: 1
Enter category (e.g., Fruits, Drinks, Stationaries, Fees): Fruits
Enter amount spent: 15
Expense added successfully!
```

**Showing Expenses:**

```
Date        Category        Amount
----------------------------------------
2025-07-25  Fruits          $15
```

**Plotting Expenses:**
A bar chart will open showing total expenses by category.

---
