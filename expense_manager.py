import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Dilli@03",
    database="expense_db"
)

cursor = conn.cursor()


class BaseExpense(ABC):

    @abstractmethod
    def add_expense(self):
        pass


class User:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def create_user(self):
        cursor.execute(
            "INSERT INTO users(name) VALUES (%s)",
            (self.__name,)
        )
        conn.commit()

        print("Created Successfully...!")
        print("User ID:", cursor.lastrowid)


class Expense(User, BaseExpense):

    def __init__(self, name):
        super().__init__(name)

    def add_expense(self, user_id, amount, category, desc):
        cursor.execute("""
            INSERT INTO expenses(user_id, amount, category, description, date)
            VALUES (%s, %s, %s, %s, CURDATE())
        """, (user_id, amount, category, desc))

        conn.commit()
        print("Expense Added successfully...!")


#========operation functions===========#

CATEGORIES = [
    "Food", "Travel", "Shopping", "Bills",
    "Health", "Entertainment", "Education", "Other"
]


def show_categories():
    print("\nSelect Category:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")


def get_category_choice():
    while True:
        try:
            show_categories()
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print("nvalid choice")
        except:
            print("Enter valid number")


def show_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\nUsers:")
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]}")


def view_expenses(user_id):
    cursor.execute("""
        SELECT e.exp_id, u.name, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
    """, (user_id,))

    data = cursor.fetchall()

    if not data:
        print("No expenses found")
        return []

    print("\nYour Expenses List:")

    for row in data:
        print(f"""
ID: {row[0]}
Name: {row[1]}
Amount: {row[2]}
Category: {row[3]}
Description: {row[4]}
Date: {row[5]}
------------------------
""")

    return data


def filter_by_category(expenses, category):
    return list(filter(lambda x: x[3] == category, expenses))


def filter_by_date(expenses, date):
    return [exp for exp in expenses if str(exp[5]) == date]


def total_expense(expenses):
    return reduce(lambda x, y: x + y, map(lambda x: x[2], expenses), 0)


def category_spending(expenses):
    categories = {exp[3] for exp in expenses}
    return {
        cat: sum(e[2] for e in expenses if e[3] == cat)
        for cat in categories
    }


def monthly_report(expenses):
    report = {}
    for exp in expenses:
        month = exp[5].month
        report[month] = report.get(month, 0) + exp[2]
    return report


def highest_expense(expenses):
    return reduce(lambda x, y: x if x[2] > y[2] else y, expenses)


def smart_insight(expenses):
    data = category_spending(expenses)
    max_cat = max(data, key=data.get)
    return f"You are spending too much on {max_cat}"


def update_expense(exp_id, amount):
    cursor.execute(
        "UPDATE expenses SET amount=%s WHERE exp_id=%s",
        (amount, exp_id)
    )
    conn.commit()
    print("Updated Successfully...!")


def delete_expense(exp_id):
    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()
    print("Deleted Successfully...!")


#========MAIN MEN===========#

while True:
    print("""
===== Smart Expense Manager =====

1. Create User
2. Add Expense
3. View Expenses
4. Filter by Category
5. Filter by Date
6. Total Expense
7. Category-wise Spending
8. Monthly Report
9. Highest Expense
10. Smart Insight
11. Update Expense
12. Delete Expense
13. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        User(name).create_user()

    elif choice == 2:
        show_users()
        user_id = int(input("Enter user id: "))

        amount = float(input("Amount: "))
        category = get_category_choice()
        desc = input("Description: ")

        Expense("temp").add_expense(user_id, amount, category, desc)

    elif choice == 3:
        show_users()
        user_id = int(input("Enter user id: "))
        view_expenses(user_id)

    elif choice == 4:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        cat = input("Enter category: ")
        print(filter_by_category(expenses, cat))

    elif choice == 5:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        date = input("Enter date (YYYY-MM-DD): ")
        print(filter_by_date(expenses, date))

    elif choice == 6:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        print("Total:", total_expense(expenses))

    elif choice == 7:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        print(category_spending(expenses))

    elif choice == 8:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        print(monthly_report(expenses))

    elif choice == 9:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        print(highest_expense(expenses))

    elif choice == 10:
        show_users()
        user_id = int(input("Enter user id: "))
        expenses = view_expenses(user_id)

        print(smart_insight(expenses))

    elif choice == 11:
        show_users()
        user_id = int(input("Enter user id: "))
        view_expenses(user_id)

        exp_id = int(input("Enter Expense ID: "))
        amount = float(input("Enter new amount: "))

        update_expense(exp_id, amount)

    elif choice == 12:
        show_users()
        user_id = int(input("Enter user id: "))
        view_expenses(user_id)
        exp_id = int(input("Enter Expense ID: "))
        delete_expense(exp_id)

    elif choice == 13:
        print("Thanks GoodBye...!")
        break

    else:
        print("Invalid choice")