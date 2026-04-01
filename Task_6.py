#TASK 1 :- ENCAPSULATION 
class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")
u1 = User()
u1.set_user("john", "1234")
u1.register()
u1.login()

# TASK 2 : INHERITANCE
class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.login()
f.faculty_greet()

tf = TempFaculty()
tf.register()
tf.login()
tf.faculty_greet()
tf.tempFaculty_greet()

# TASK 3 : METHOD OVERRIDING

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

s = Student()
f = Faculty()

s.greet()
f.greet()

# TASK 4 : METHOD CHAINING

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

user = User()
user.login().greet().register()

# TASK 5 : MINI USER SYSTEM

class User:
    users_count = 0  

    def __init__(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        User.users_count += 1

    def get_username(self):
        return self.__username

    def register(self):
        print(f"{self.__username} registered")
        return self

    def login(self):
        print(f"{self.__username} logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self

s1 = Student("john", "123")
f1 = Faculty("admin", "456")

s1.login().greet().register()
f1.login().greet().register()

print("Total Users:", User.users_count)