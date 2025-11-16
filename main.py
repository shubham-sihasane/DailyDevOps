# A simple practice diary of Python

# print("Hello World!")
# print("Welcome to the world of Python Programming.")
#
# name = "shubham sihasane"
# print(name)
# print(type(name))
#
# age = 30
# print(age)
# print(type(age))
#
# price = 11.99
# print(price)
# print(type(price))
#
# is_active = True
# print(is_active)
# print(type(is_active))
#
# comp = 2 + 5j
# print(comp)
# print(type(comp))
#
# int_num = 25
# float_num = 11.99
# total = int_num + float_num
# print(total)
# print(type(total))

# print(int(12.50))
# print(type(int(12.50)))
#
# print(float(11))
# print(type(float(11)))
#
# print(str(25))
# print(type(str(25)))
#
# print(int("100"))
# print(type(int("100")))

# print("Hello" + " " + "World!")

# print("Hello", "World", end="===", sep=" - ")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# price = float(input("Enter your price: "))
# print(f"Hello, {name}\nYou are {age} years old.\nYour value is {price}.")

# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
#
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# floor_division = num1 // num2
# exponent = num1 ** num2
# print(f"Addition         {num1} + {num2} = {addition}")
# print(f"Subtraction      {num1} - {num2} = {subtraction}")
# print(f"Multiplication   {num1} * {num2} = {multiplication}")
# print(f"Division         {num1} / {num2} = {division}")
# print(f"Floor Division   {num1} // {num2} = {floor_division}")
# print(f"Power            {num1} ^ {num2} = {exponent}")
# = | += | -= | *= | /= | //= | **=

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print("num1 == num2 = ", num1 == num2)
# print("num1 != num2 = ", num1 != num2)
# print("num1 > num2  = ", num1 > num2)
# print("num1 < num2  = ", num1 < num2)
# print("num1 >= num2 = ", num1 >= num2)
# print("num1 <= num2 = ", num1 <= num2)

# print(num1 == 0 and num2 == 0)
# print(num1 == 0 or num2 == 0)
# print(not num1 == num2)

# def bill_split(bill, friend):
#     total = bill + ((bill * 20) / 100)
#     subtotal = total / friends
#     print(f"The split amount: {subtotal}")
#
# amount = float(input("Enter the amount: "))
# friends = int(input("Enter the number of friends: "))
#
# bill_split(amount, friends)

# number = int(input("Enter a number: "))
# if number > 0:
#     print("It is positive number.")
# else:
#     print("It is negative number.")

# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive Number.")
# elif number < 0:
#     print("Negative Number.")
# else:
#     print("Zero Number.")

# number = int(input("Enter a number: "))
# if number >= 0:
#     if number > 0:
#         print("Positive number.")
#     elif number == 0:
#         print("Zero number.")
# else:
#     print("Negative number.")

# age = int(input("Enter your age: "))
# salary = float(input("Enter your salary: "))
#
# if age >= 18 and salary >= 50000:
#     print("You are eligible for membership.")
# else:
#     print("You are not eligible for membership.")

# def pass_fail(marks):
#     if marks >= 50:
#         return "Pass"
#     else:
#         return "Fail"
#
# print(pass_fail(30))

# fruits = ["apple", "banana", "orange", "mango"]
# for fruit in fruits:
#     print("I love " + fruit)

# name = "shubham sihasane"
# for char in name:
#     print(char, sep=" ", end=" ")

# for num in range(1, 11):
#     print(num, end=" ")

# for num in range(1, 11):
#     if num == 5:
#         break
#     print(num, end=" ")

# print()

# for num in range(1, 11):
#     if num == 5:
#         continue
#     print(num, end=" ")

# for i in range(1,11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print()

# for _ in range(1, 11):
#     print("Hi", end=" ")

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print(f"The factorial of {num} is {fact}")

# counter = 1
# while counter <= 5:
#     print("The value of " + str(counter))
#     counter += 1

# secret = 100
# num = int(input("Enter a number: "))
# while num != secret:
#     num = int(input("Enter a number: "))
# else:
#     print("Congratulations.")

# while True:
#     user = input("Enter your name: (x to end): ")
#     if user == "x":
#         break
#     print(f"Hey, {user}")

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=' ')
#
# print()
#
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i, end=' ')

# def sum_greater_than(numbers, num):
#     addition = 0
#     for n in numbers:
#         if n > num:
#             addition += n
#     return addition
# total = sum_greater_than([2,4,6,8,10],5)
# print(f"The addition of numbers greater than 5 is {total}")

# def funny_story():
#     pass
#
# class Students:
#     pass

# print(0b1101011)  # prints 107
#
# print(0xFB + 0b10)  # prints 253
#
# print(0o15)  # prints 13

# import random
#
# print(random.randint(1,100))
# print(random.randrange(1,100))
#
# friends = ['shubham', 'omkar', 'manoj','rashmi']
# print(random.choice(friends))
# print(friends)
# random.shuffle(friends)
# print(friends)

# import math
# print(math.pi)
# print(math.cos(math.pi))
# print(math.exp(10))
# print(math.log10(1000))
# print(math.sinh(1))
# print(math.factorial(6))

# import math
# def calculate_circle_area(radius):
#     if radius < 0:
#         print("Radius cannot be negative.")
#     return (math.pi * (radius ** 2))
#
# # Example usage:
# radius_value = float(input("Enter radius: "))
# area_of_circle = calculate_circle_area(radius_value)
# print(f"The area of a circle with radius {radius_value} is: {area_of_circle}")

# fruits = ["apple", "mango", "banana", "pineapple", "apple"]
# friends = ["shubham", "omkar", "manoj"]
# print(fruits)
#
# for fruit in fruits:
#     print("I love " + fruit)
#
# print(f"The first item is {fruits[0]}")
# print(f"The last item is {fruits[-1]}")
# print(f"The list of items is {fruits[:]}")
# print(f"The items from 0th to 2nd item is {fruits[:3]}")
# print(f"The items from 1st to 3rd item is {fruits[1:3]}")

# fruits[3] = "jackfruit"
# print(fruits)
# fruits.append("orange")
# print(fruits)
#
# fruits.remove("apple")
# print(fruits)
#
# fruits.insert(4, "apple")
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# fruits.sort()
# print(fruits)
#
# fruits.sort(reverse=True)
# print(fruits)
#
# fruits.pop()
# print(fruits)

# fruits.extend(friends)
# print(fruits)

# fruits.clear()
# print(fruits)

# del friends[1]
# print(friends)
#
# del friends
# print(friends) # Error as friends list deleted

# print(f"The number of fruits: {len(fruits)}")

# print(f"The count of apples is {fruits.count("apple")}")

# fals = fruits.copy()
# print(fals)

