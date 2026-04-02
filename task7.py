from abc import ABC, abstractmethod
from functools import reduce

# Task 2: Abstraction
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Task 1: super()
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"Temp Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration} months"

students = [
    Student("Dilli", 1, "CSE", 60000),
    Student("Sai", 2, "ECE", 40000),
    Student("Ram", 3, "IT", 80000)
]

faculty = [
    Faculty("john", 101, 50000),
    Faculty("Divya", 102, 25000),
    TempFaculty("Ramesh", 103, 30000, 6)
]


print("----- ALL DETAILS -----")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())


# Task 3: Sorting
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\n----- SORTED STUDENTS (by fees) -----")
for s in students:
    print(s.name, s.fees)

print("\n----- SORTED FACULTY (by salary) -----")
for f in faculty:
    print(f.name, f.salary)


# Task 4: map()
student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)


# Task 5: filter()
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHigh Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)


# Task 6: reduce()
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)


# Task 7: Higher Order Function
def process_users(users, func):
    return list(map(func, users))
names_upper = process_users(students, lambda s: s.name.upper())
print("\nProcessed Names (Uppercase):", names_upper)