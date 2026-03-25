# Mini Project 1: Employee Management System

employees = []

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        role = input("Role: ")
        salary = float(input("Salary: "))
        employees.append({"name":name,"age":age,"role":role,"salary":salary})

    elif choice == "2":
        for e in employees:
            print(e)

    elif choice == "3":
        name = input("Enter name to update: ")
        for e in employees:
            if e["name"] == name:
                e["role"] = input("New role: ")
                e["salary"] = float(input("New salary: "))

    elif choice == "4":
        name = input("Enter name to delete: ")
        for e in employees:
            if e["name"] == name:
                employees.remove(e)

    elif choice == "5":
        break



# Mini Project 2: Student Report Card

name = input("Enter student name: ")
m1 = int(input("Subject1: "))
m2 = int(input("Subject2: "))
m3 = int(input("Subject3: "))

total = m1 + m2 + m3
avg = total / 3

print("\nReport Card")
print("Name:", name)
print("Total:", total)
print("Average: {:.2f}".format(avg))

if avg >= 75:
    print("Grade: A")
elif avg >= 50:
    print("Grade: B")
else:
    print("Grade: C")



#  Mini Project 3: Shopping Cart System

cart = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Total 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Product: ")
        price = float(input("Price: "))
        qty = int(input("Qty: "))
        cart.append({"name":name,"price":price,"qty":qty})

    elif ch == "2":
        for i in cart:
            print(i)

    elif ch == "3":
        name = input("Remove product: ")
        for i in cart:
            if i["name"] == name:
                cart.remove(i)

    elif ch == "4":
        total = 0
        for i in cart:
            total += i["price"] * i["qty"]
        print("Total Bill:", total)

    elif ch == "5":
        break



# Mini Project 4: Login & User Validation

users = {"admin":"1234","user":"1111"}

u = input("Username: ")
p = input("Password: ")

if u in users and users[u] == p:
    print("Login Success")
else:
    print("Invalid Login")



# Mini Project 5: Unique Visitor Counter

visitors = set()

while True:
    name = input("Enter visitor name (or exit): ")
    if name == "exit":
        break
    visitors.add(name)

print("Unique visitors:", len(visitors))
print(visitors)



#  Mini Project 6: String Formatter Tool

name = input("Enter name: ")
product = input("Enter product: ")

print("{} bought {}".format(name, product))

print("Left  : {:<10}".format(name))
print("Right : {:>10}".format(name))
print("Center: {:^10}".format(name))



#  Mini Project 7: Bank Account System

account = {"name":"", "balance":0}

account["name"] = input("Enter name: ")
account["balance"] = float(input("Initial balance: "))

while True:
    print("\n1.Deposit 2.Withdraw 3.Check 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        amt = float(input("Amount: "))
        account["balance"] += amt

    elif ch == "2":
        amt = float(input("Amount: "))
        if amt <= account["balance"]:
            account["balance"] -= amt
        else:
            print("Insufficient balance")

    elif ch == "3":
        print("Balance:", account["balance"])

    elif ch == "4":
        break


# Mini Project 8: Voting System

votes = {"A":0,"B":0,"C":0}

while True:
    v = input("Vote (A/B/C or exit): ")
    if v == "exit":
        break
    if v in votes:
        votes[v] += 1

print(votes)

winner = max(votes, key=votes.get)
print("Winner:", winner)



#Mini Project 9: Course Enrollment System

students = {}

name = input("Student name: ")
courses = input("Enter courses (comma): ").split(",")

students[name] = courses

print("Student Details:")
for s in students:
    print(s, students[s])



#Mini Project 10: Number Utility Tool

num = int(input("Enter number: "))

print("Binary: {:b}".format(num))
print("Binary: {:o}".format(num))
print("Binary: {:h}".format(num))
print("With commas: {:,}".format(num))
print("Scientific: {:.2e}".format(num))