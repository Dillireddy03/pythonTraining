#1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i, end=" ")
print("\n")

#2. Print even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i, end=" ")

print("\n")

#3. Print odd numbers from 1 to 100
for i in range(1, 101, 2):
    print(i, end=" ")
print("\n")

# 4. Multiplication table of 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
print("\n")
#5. Sum of numbers from 1 to 100
total_sum = sum(range(1, 101))
print("Sum of numbers from 1 to 100:", total_sum)

#6. Reverse numbers from 50 to 1
for i in range(50, 0, -1):
    print(i, end=" ")
print("\n")
#7. Count numbers divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)  

#8. Squares of numbers from 1 to 10
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")

#9. Cubes of first 10 numbers
for i in range(1, 11):
    print(f"{i}^3 = {i**3}")

#10. Take input n, print 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")
#11. Print numbers 1 to 20 using while loop
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print("\n")
#12. Factorial using while
num = int(input("Enter a number to find factorial: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"Factorial of {num} is {factorial}")

#13. Reverse a number using while
num = int(input("Enter a number to reverse: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

#14. Count digits using while
num = int(input("Enter a number to count digits: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)

#15. Keep asking input until "stop" using while
while True:
    user = input("say something(type stop to stop): ")
    if user.lower() == "stop":
        break

#16. Pattern *
for i in range(1, 5):
    print("*" * i)

#17. Pattern numbers
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

#18. Multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end="  ")
        print("\n")
    print()

#19. Print A B C pattern
for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()
print("\n")
#20. Matrix pattern
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

#21. Count total characters in a string
string = input("Enter a string to find length: ")
print("Total characters:", len(string)) 

#22. Count vowels in a string
s = input("enter string to count vowels :-")
vowels = "aeiou"
count = 0

for i in s:
    if i in vowels:
        count += 1

print(count)

#23. Count consonants in a string
s = input("enter string to count consonants :-")
vowels = "aeiou"
count = 0

for i in s:
    if i not in vowels:
        count += 1

print(count)

#24. Reverse a string using loop
s = input("enter a string to reverse :-")
reverse = ""
for i in s:
    reverse = i + reverse
print(reverse)

#25. Check if string is palindrome
s = input("enter a string check either it is palindrome or not :-")
reverse = ""
for i in s:
    reverse = i + reverse
if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#26. Print first 5 characters
s = "dilli reddy"
print(s[:5])

#27. Print last 3 characters
s = "dilli reddy"
print(s[-3:])

#28. Reverse string using slicing
s = "dilli reddy"
print(s[::-1])

#29. Print every 2nd character
s = "dilli reddy"
print(s[::2])

#30. Remove first and last character
s = "dilli reddy"
print(s[1:-1])

#31. Create list and find sum
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for i in numbers:
    total_sum += i
print("Sum of the list:", total_sum)        

#32. Find maximum value in a list
numbers = [1, 2, 3, 4, 5]
max_value = numbers[0]  
for i in numbers:
    if i > max_value:
        max_value = i
print("Maximum value:", max_value)

#33. Find minimum value in a list
numbers = [1, 2, 3, 4, 5]
min_value = numbers[0]
for i in numbers:
    if i < min_value:
        min_value = i
print("Minimum value:", min_value)

#34. Count total elements in a list
numbers = [1, 2, 3, 4, 5]
count = 0
for i in numbers:
    count += 1
print("Total elements:", count)

#35. Check if element exists in a list
numbers = [1, 2, 3, 4, 5]   
element = input("enter element to check existence :-")
exists = False
for i in numbers:
    if i == element:
        exists = True
        break
print("Element exists:", exists)

#36. Add elements using append()
l = [1, 2]
l.append(3)
l.append(4)
l.append(5)

print(l)

#37. Insert element at index
l = [11, 22, 55, 66]
l.insert(2,3)
print(l)

#38. Remove element using remove()
l = [1, 2, 3, 4, 5]
l.remove(3)
print(l)

#39. Reverse list without using .reverse()
l = [1, 2, 3, 4, 5]
reverse = []
for i in l:
    reverse = [i] + reverse
print(reverse)

#40. Sort list without using .sort()
l = [8, 2, 7, 1, 5]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)
