#  Task 1: User Info Manager (Functions + Dictionary)
rangee = int(input("enter no of users data to be added : "))
def create_user(name,age,role):
    return {
        "name" : name.title() ,
        "age" : age ,
        "role" : role
    }
users = []
if rangee == 0 :
    print("there is no reecords to add")
else :
    for i in range(rangee):
        name = input("enter your name :")
        age = input("enter your age :")
        role = input("enter the role :")
        users.append(create_user(name,age,role))
    
print(users)


# Task 2: Dynamic Calculator (*args)
numb = int(input("enter noOf numbers to sum : "))
num = []
for i in range(numb):
   num.append(int(input("enter number : ")))
my_tup = tuple(num)
print(my_tup)

def calculate_numbers(*my_tup) :
    total = sum(my_tup)
    average = total/len(my_tup)
    return total , average

result = calculate_numbers(*my_tup)
print("sum of {} numbers is : " .format(numb), result[0])
print("average of {} number is : ".format(numb), result[1])


#  Task 3: Keyword Config System (**kwargs)
def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")
system_config(mode="testing", version="2.45.67", user="tester")


#  Task 4: Factorial Service (Recursion)
n = int(input("enter the number to find factorial :"))
def factorial(n) :
    if n == 0 or n == 1:
  
        return 1
    elif n <= 0 :
        print("invalid input ")
    else :
        return n*factorial(n-1)
print(factorial(n))


#  Task 5: Memory Optimization (Generator)
n = int(input("enter number to square upto : "))
def square_generator(n):
    for i in range(1,n+1):
        yield i * i
square_generator(n)
for i in square_generator(n):
    print(i)
print(type(square_generator(n)))
print(list(square_generator(n)))
print(type(list(square_generator(n))))


# Task 6: Exception Handling Module
numerator = int(input("enter the numerator number : "))
denominator = int(input("enter the denominator number : "))
try :
    result = numerator / denominator
    print(result)
except ZeroDivisionError :
    print("unable to divide with zero")
except Exception :
    print("please enter VALID input ")
finally :
    print("program completed")


#  Task 7: File Handling
with open("team_data.txt","w") as f:
    f.write("HI..!This is 'Hema Sai' ,\n")
    f.write("My Designation is 'Analyst'\n")
    f.write("I am from kerala\n")
    f.closed
with open("team_data.txt","r") as f:
    print(f.read())
    print(f.closed)
