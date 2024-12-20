# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# If else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# IF-elif-else statement
x = 5
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less than 5")

# For loop
for i in range(3):
    print("Loop iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Nested Loop
for i in range(2):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Break, Continue and Pass
for i in range(5):
    if i == 4:
        break  # exits loop if i is 4
    elif i == 1:
        continue  # skips this iteration if i is 1
    print(i)

# Input & Output
name = input("Enter your name: ")
print("Hello,", name)

# Introduction to Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# List, Methods and slicing
fruit = ["apple", "banana", "cherry"]
fruit.append("orange")  # Adds "orange"
print(fruit)       

# Introduction to Dictionaries & Dictionary Methods
person = {"name": "Sarthak", "age": 22}
print(person["name"])  

# Introduction to Set & Set Methods
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# Introduction to Map & Map Methods
numbers = [1, 2, 3]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  
