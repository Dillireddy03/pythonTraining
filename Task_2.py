#prob-1
a = 10
b = 6
print(a&b)
# prob - 2
x = 12
y = 5
print(x|y)
#prob - 3
num = 8
print(~num)
#prob - 4
a = 15
b = 9
print(a^b)

#prob - 5
num = 7
print(num<<2)

#prob - 6
num = 20
print(num>>1)

#prob - 7 , 8
num1 = int(input("enter number 1:-"))
num2 = int(input("enter number 2:-"))
print (num1 & num2)

#prob - 8
num11 = int(input("enter number 1:-"))
num22 = int(input("enter number 2:-"))
print (num1 ^ num2)

#prob - 9 
h = "hi"
print(h*4)

#prob - 10
k = "python"
print(h*3)

#prob - 11
str1 = "super"
str2 = "man"
print(str1 + str2)

#prob - 12
st1 = "hello"
st2 = " "
st3 = "world"
print(st1 + st2 + st3)

#prob - 13
name = input("enter your name :- ")
print(name*5)

#prob - 14
name1 = input("enter name 1 :- ")
name2 = input("enter name 2 :- ")
print(name1 + name2)

#prob - 15
nam = input("enter input :-")
print(type(nam))

#prob - 16
age = input("enter your age :-")
int(age)
print(age)

#prob - 17
num1 = int(input("enter number 1 :- "))
num2 = int(input("enter number 2 :- "))
print(num1 + num2)

#prob - 18
mark1 = int(input("enter mark 1 :- "))
mark2 = int(input("enter mark 2 :- "))
print((mark1 + mark2) / 2)

#prob - 19
a = int(input("enter number a :- "))
b = int(input("enter number b :- "))

print(3 * a * 2 + b - 2)

#prob - 20
num = input("enter a number :- ")

print(type(num))

num = int(num)

print(type(num))

#prob - 21
num = input("enter a number :- ")
print(num[-1])

#prob - 22
num = int(input("enter a number :- "))
print(num % 10)

#prob - 23
num = int(input("enter a number :- "))
print(num // 10)

#prob - 24
num = int(input("enter a number :- "))
print((num // 10) % 10)

#prob - 25
num = int(input("enter 5 digit number :- "))
print(num % 10)

#prob - 26
if 10 >= 5:
    print("10 is greater than or equal to 5")

#prob - 27
num = int(input("enter number :- "))
if num > 50:
    print("number is greater than 50")

#prob - 28
age = int(input("enter age :- "))
if age >= 18:
    print("eligible")

#prob - 29
num = int(input("enter number :- "))
if num > 100:
    print("number is greater than 100")

#prob - 30
num = int(input("enter number :- "))
if num >= 0:
    print("number is greater")

#prob - 31
num = int(input("enter number :- "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#prob - 32
marks = int(input("enter marks :- "))
if marks >= 35:
    print("pass")
else:
    print("fail")

#prob - 33
num = int(input("enter number :- "))
if num >= 0:
    print("positive")
else:
    print("negative")
    
#prob - 34
num = int(input("enter number :- "))
if num > 10:
    print("greater than 10")
else:
    print("not greater than 10")

#prob - 35
age = int(input("enter age :- "))
height = int(input("enter height :- "))
weight = int(input("enter weight :- "))
if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("selected")
        else:
            print("rejected")
    else:
        print("rejected")
else:
    print("rejected")

#prob - 36
marks = int(input("enter marks :- "))
age = int(input("enter age :- "))

if marks >= 60:
    if age >= 17:
        print("admission granted")
    else:
        print("not eligible")
else:
    print("not eligible")

#prob - 37
age = int(input("enter age :- "))
height = int(input("enter height :- "))
weight = int(input("enter weight :- "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("selected")
        else:
            print("rejected")
    else:
        print("rejected")
else:
    print("rejected")

#prob - 38
day = int(input("enter number (1-7):- "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")

#prob - 39
num = int(input("enter number (1-3):- "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

#prob - 40
num = int(input("enter number (1-4):- "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")